from sage.sat.solvers.dimacs import DIMACS
from sage.all import *
from sage.combinat.posets.poset_examples import Posets
import itertools

import sage.libs.ecl
sage.libs.ecl.ecl_eval("(ext:set-limit 'ext:heap-size 0)")

from enum import Enum

class VarType(Enum): 
    IsLess = 1
    IsMore = 2
    IsUsed = 3
    IsEvenly = 4

def construct_variable_map(poset, linear_extensions_count, expected_ldim):
    '''
    is_lower[a, b, i]  > 0 means that a < b in the i-th ple
    is_higher[a, b, i] > 0 means that a > b in the i-th ple
    Is_used[a, i]      > 0 means that a is in the i-th ple
    Is_evenly[a, i, j] > 0 means that among first a elements from P there is at least i that are present in j-th ple 
    '''
    variable_idx = 1

    elements = len(poset)
    all_elements = elements * expected_ldim
    if(all_elements % linear_extensions_count != 0):
        raise Exception("CANNOT DO EVENLY")
    in_each_ple = all_elements // linear_extensions_count

    is_lower = {}    
    for a,b in itertools.combinations(poset, int(2)):
        for i in range(linear_extensions_count):
            is_lower[a,b,i] = variable_idx
            variable_idx += 1

    is_higher = {}    
    for a,b in itertools.combinations(poset, int(2)):
        for i in range(linear_extensions_count):
            is_higher[a,b,i] = variable_idx
            variable_idx += 1

    is_used = {}    
    for a in poset:
        for i in range(linear_extensions_count):
            is_used[a, i] = variable_idx
            variable_idx += 1


    Is_evenly = {}    
    for a in range(elements):
        for i in range(elements):
            for j in range(linear_extensions_count):
                Is_evenly[a, i, j] = variable_idx
                variable_idx += 1

    def is_less_variable_getter(*args):
        a, b, i = args
        if b < a:
            raise Exception("b < a")
        return is_lower[a,b,i]

    def is_more_variable_getter(*args):
        a, b, i = args
        if b < a:
            raise Exception("b < a")
        return is_higher[a,b,i]

    def is_used_variable_getter(*args):
        a, i = args
        return is_used[a, i]

    def is_even_variable_getter(*args):
        i, i, j = args
        return Is_evenly[a, i, j]

    def variable_getter(VarType, *args):
        match VarType:
            case VarType.IsLess: return is_less_variable_getter(*args)
            case VarType.IsMore: return is_more_variable_getter(*args)
            case VarType.IsUsed: return is_used_variable_getter(*args)
            case VarType.IsEvenly: return is_even_variable_getter(*args)
            case _: raise Exception("Unknown variable type")
        
    return variable_getter

def get_boolean_graph(dim):
    B = Posets.BooleanLattice(dim)
    return DiGraph([x for x in B.relations() if x[0] != x[1]])
