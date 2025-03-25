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

def construct_variable_map(poset, linear_extensions_count):
    '''
    is_lower[a, b, i]  > 0 means that a < b in the i-th linear extension
    is_higher[a, b, i] > 0 means that a > b in the i-th linear extension
    Is_used[a, i]      > 0 means that a is in the i-th linear extension
    '''
    variable_idx = 1

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

    def variable_getter(VarType, *args):
        match VarType:
            case VarType.IsLess: return is_less_variable_getter(*args)
            case VarType.IsMore: return is_more_variable_getter(*args)
            case VarType.IsUsed: return is_used_variable_getter(*args)
            case _: raise Exception("Unknown variable type")
        
    return variable_getter

def get_transitivity_clauses(poset, linear_extensions_count, var_getter):
    '''
    In each linear extension and each a, b, c that are used:
        (a > b or b > c or a < c)
    Because if a < b and b < c that implies a < c
    '''

    clauses = []

    for a, b, c in itertools.combinations(poset, int(3)):
        for i in range(linear_extensions_count):
            use_a = var_getter(VarType.IsUsed, a, i)
            use_b = var_getter(VarType.IsUsed, b, i)
            use_c = var_getter(VarType.IsUsed, c, i)
            a_less_b = var_getter(VarType.IsLess, a, b, i)
            b_less_c = var_getter(VarType.IsLess, b, c, i)
            a_less_c = var_getter(VarType.IsLess, a, c, i)
            clauses.append((-use_a, -use_b, -use_c, -a_less_b, -b_less_c, a_less_c))

    for a, b, c in itertools.combinations(poset, int(3)):
        for i in range(linear_extensions_count):
            use_a = var_getter(VarType.IsUsed, a, i)
            use_b = var_getter(VarType.IsUsed, b, i)
            use_c = var_getter(VarType.IsUsed, c, i)
            a_more_b = var_getter(VarType.IsMore, a, b, i)
            b_more_c = var_getter(VarType.IsMore, b, c, i)
            a_more_c = var_getter(VarType.IsMore, a, c, i)
            clauses.append((-use_a, -use_b, -use_c, -a_more_b, -b_more_c, a_more_c))

    return clauses

def generate_use_clauses(poset, linear_extensions_count, local_dim, var_getter):
    '''
    1. a < b => a is used and b is used
    2. a > b => a is used and b is used 
    3. if a and b are used then a < b or a > b
    4. a is used at most local_dim times
    5. in each ple there is 12 elements 
    '''
    
    clauses = []

    for a, b in itertools.combinations(poset, int(2)):
        for i in range(linear_extensions_count):
            is_lower = var_getter(VarType.IsLess, a, b, i)
            is_used_a = var_getter(VarType.IsUsed, a, i)
            is_used_b = var_getter(VarType.IsUsed, b, i) 
            clauses.append((is_used_a, -is_lower))
            clauses.append((is_used_b, -is_lower))

    for a, b in itertools.combinations(poset, int(2)):
        for i in range(linear_extensions_count):
            is_higher = var_getter(VarType.IsMore, a, b, i)
            is_used_a = var_getter(VarType.IsUsed, a, i)
            is_used_b = var_getter(VarType.IsUsed, b, i)
            clauses.append((is_used_a, -is_higher))
            clauses.append((is_used_b, -is_higher))
            
    for a, b in itertools.combinations(poset, int(2)):
        for i in range(linear_extensions_count):
            is_used_a = var_getter(VarType.IsUsed, a, i)
            is_used_b = var_getter(VarType.IsUsed, b, i)
            is_lower = var_getter(VarType.IsLess, a, b, i)
            is_higher = var_getter(VarType.IsMore, a, b, i)
            clauses.append((-is_used_a, -is_used_b, is_lower, is_higher))

    cannot_be_used_times = local_dim + 1
    for a in poset:
        for x in itertools.combinations(range(linear_extensions_count), int(cannot_be_used_times)):
            clauses.append(tuple([-var_getter(VarType.IsUsed, a, i) for i in x]))
 
    return clauses

def generate_poset_clauses(boolean_graph, linear_extensions_count, var_getter):
    '''
    1. Keep same order 
    2. If a || b then in one linear extension a < b and in another b < a
    '''
    
    clauses = []

    # For each a and b that a < b in Boolean Lattice there must be LE that a < b 
    for a, b in sorted(boolean_graph.edges(labels=False)):
        clauses.append(tuple([var_getter(VarType.IsLess, a, b, i) for i in range(linear_extensions_count)]))
        for i in range(linear_extensions_count):
            clauses.append(tuple([-var_getter(VarType.IsMore, a, b, i)]))
                 

    # For each a and b that a || b in Boolean Lattice
    for a in sorted(boolean_graph.vertices()):
        for b in sorted(boolean_graph.vertices()):
            if a != b and a < b and not boolean_graph.has_edge(a, b):
                one_way = [var_getter(VarType.IsLess, a, b, i) for i in range(linear_extensions_count)]
                another_way = [var_getter(VarType.IsMore, a, b, i) for i in range(linear_extensions_count)]
                clauses.append(tuple(one_way))
                clauses.append(tuple(another_way))
        
    return clauses

def generate_less_more_clauses(poset, linear_extensions_count, var_getter):
    '''
    1. a < b => !(b < a) and  b < a => !(a < b)
    '''
    
    clauses = []

    for a, b in itertools.combinations(poset, int(2)):
        for i in range(linear_extensions_count):
            is_lower = var_getter(VarType.IsLess, a, b, i)
            is_higher = var_getter(VarType.IsMore, a, b, i)
            clauses.append((-is_lower, -is_higher))
            
    return clauses

def get_boolean_graph(dim):
    B = Posets.BooleanLattice(dim)
    return DiGraph([x for x in B.relations() if x[0] != x[1]])

def generate_clauses(dim, linear_extensions_count, local_dim):
    boolean_graph = get_boolean_graph(dim)

    vertices = sorted(boolean_graph.vertices())
    var_getter = construct_variable_map(vertices, linear_extensions_count)

    clauses  = generate_poset_clauses(boolean_graph, linear_extensions_count, var_getter)
    clauses += generate_use_clauses(vertices, linear_extensions_count, local_dim, var_getter)
    clauses += generate_less_more_clauses(vertices, linear_extensions_count, var_getter)
    clauses += get_transitivity_clauses(vertices, linear_extensions_count, var_getter)

    return clauses

def save_problem(dim, local_dim, linear_extensions_count, file_name):
    clauses = generate_clauses(dim, linear_extensions_count, local_dim)

    sat_generator = DIMACS()
    for c in clauses:
        sat_generator.add_clause(c)
    sat_generator.clauses(file_name)

save_problem(
    dim = 4,
    local_dim = 3,
    linear_extensions_count = 4,
    file_name = "dim43.dimacs"
)