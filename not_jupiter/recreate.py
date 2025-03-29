from functools import cmp_to_key

from sage.sat.solvers.dimacs import DIMACS
from sage.all import *
from sage.combinat.posets.poset_examples import Posets
import itertools

import sage.libs.ecl
sage.libs.ecl.ecl_eval("(ext:set-limit 'ext:heap-size 0)")

from enum import Enum

from common_vars import construct_variable_map, VarType, get_boolean_graph

def to_str(x):
    str = ''

    current_letter = 'a'
    current_number = 1

    while current_number <= x:
        if x & current_number:
            str += current_letter
        current_number *= 2
        current_letter = chr(ord(current_letter) + 1)      
     

    has_any_letter = any(c.isalpha() for c in str) 
    return str if has_any_letter else "(/)"

def recover_order(values, variables, n, lin_ext_idx):
    is_used = lambda x: values[variables(VarType.IsUsed, x, lin_ext_idx)] > 0
    ordering = list(filter(is_used,[e for e in range(1 << n)]))
    

    def Compare(a, b):
        was_reversed = False
        if a > b:
            a, b = b, a
            was_reversed = True
        is_lower = values[variables(VarType.IsLess, a, b, lin_ext_idx)]
        is_higher = values[variables(VarType.IsMore, a, b, lin_ext_idx)]

        multiplier = 1 if not was_reversed else -1
        if is_lower:
            return -1 * multiplier
        if is_higher:
            return 1 * multiplier
        
    return sorted(ordering, key=cmp_to_key(Compare))

def to_list(data):
    return [0] + sum(list(map(lambda x:  x.strip().split(' ')[1:], data.split("\n"))), [])

def to_map(list_data):
    values = {i:int(list_data[i]) > 0 for i in range(len(list_data))}
    values.update({-i : not (int(list_data[i]) > 0) for i in range(len(list_data))})
    return values

def parse_solution(n, le_count, ldim, data, should_to_string = False):
    variables = construct_variable_map(sorted(get_boolean_graph(n).vertices()), le_count, ldim)
    values = to_map(to_list(data))
    result = [recover_order(values, variables, n, j) for j in range(le_count)]
    if should_to_string:
        return [list(map(to_str, x)) for x in result]
    return result

file = "xd.txt"
data = open(file, "r").read()


result = parse_solution(6, 16, 4, data, False)

print(result)