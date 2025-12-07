from sage.sat.solvers.dimacs import DIMACS
import itertools

import sage.libs.ecl

sage.libs.ecl.ecl_eval("(ext:set-limit 'ext:heap-size 0)")

from sat_vars import construct_variable_map, VarType, get_boolean_graph
from from_sat import parse_solution


def generate_transitivity_clauses(poset, linear_extensions_count, var_getter):
    """
    In each linear extension and each a, b, c that are used:
        (a > b or b > c or a < c)
    Because if a < b and b < c that implies a < c
    """

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
    """
    1. a < b => a is used and b is used
    2. a > b => a is used and b is used
    3. if a and b are used then a < b or a > b
    4. a is used at most local_dim times
    """

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
        for x in itertools.combinations(
            range(linear_extensions_count), int(cannot_be_used_times)
        ):
            clauses.append(tuple([-var_getter(VarType.IsUsed, a, i) for i in x]))

    return clauses


def generate_poset_clauses(boolean_graph, linear_extensions_count, n, var_getter):
    """
    1. Keep same order
    2. If a || b then in one linear extension a < b and in another b < a
    """

    clauses = []

    singletons = [1 << i for i in range(n + 2)]

    # For each a and b that a < b in Boolean Lattice there must be LE that a < b
    for a, b in sorted(boolean_graph.edges(labels=False)):
        if (a in singletons and b not in singletons) or a == 0:
            less_v = lambda i: var_getter(VarType.IsLess, a, b, i)
            less_in_any = [less_v(i) for i in range(linear_extensions_count)]
            #clauses.append(tuple(less_in_any))
            for i in range(linear_extensions_count):
                clauses.append(tuple([-var_getter(VarType.IsMore, a, b, i)]))

    # For each a and b that a || b in Boolean Lattice
    for a in sorted(boolean_graph.vertices()):
        for b in sorted(boolean_graph.vertices()):
            if (
                (a in singletons and b not in singletons)
                or (a not in singletons and b in singletons)
                or a == 0
            ):
                if a != b and a < b and not boolean_graph.has_edge(a, b):
                    one_way = [
                        var_getter(VarType.IsLess, a, b, i)
                        for i in range(linear_extensions_count)
                    ]
                    another_way = [
                        var_getter(VarType.IsMore, a, b, i)
                        for i in range(linear_extensions_count)
                    ]
                    clauses.append(tuple(one_way))
                    clauses.append(tuple(another_way))

    return clauses


def generate_less_more_clauses(poset, linear_extensions_count, var_getter):
    """
    1. a < b => !(b < a) and  b < a => !(a < b)
    """

    clauses = []

    for a, b in itertools.combinations(poset, int(2)):
        for i in range(linear_extensions_count):
            is_lower = var_getter(VarType.IsLess, a, b, i)
            is_higher = var_getter(VarType.IsMore, a, b, i)
            clauses.append((-is_lower, -is_higher))

    return clauses


def generate_even_in_ple_clauses(
    poset, linear_extensions_count, expected_ldim, var_getter
):
    """
    at most X elements in ple
    """

    clauses = []

    elements = len(poset)
    all_elements = elements * expected_ldim
    in_each_ple = all_elements // linear_extensions_count

    cannot_be_used_times = in_each_ple + 1
    for i in range(linear_extensions_count):
        used_vars = [var_getter(VarType.IsUsed, a, i) for a in poset]
        for x in itertools.combinations(
            range(len(used_vars)), int(cannot_be_used_times)
        ):
            clauses.append(tuple([-used_vars[i] for i in x]))

    return clauses


def force_from(var_getter, filename, forced_n, forced_ple, forced_ldim):
    result = parse_solution(
        n=forced_n,
        le_count=forced_ple,
        data=open(filename, "r").read(),
        should_to_string=False,
    )

    clauses = []
    for ple_idx in range(len(result)):
        for a, b in zip(result[ple_idx], result[ple_idx][1:]):
            if a < b:
                clauses.append(tuple([var_getter(VarType.IsLess, a, b, ple_idx)]))
            else:
                clauses.append(tuple([var_getter(VarType.IsMore, b, a, ple_idx)]))
    return clauses


def generate_at_least_n_used(poset, linear_extensions_count, expected_ldim, var_getter):

    clauses = []

    cannot_be_used_times = len(poset) - 2
    for i in range(linear_extensions_count):
        used_vars = [var_getter(VarType.IsUsed, a, i) for a in poset]
        for x in itertools.combinations(
            range(len(used_vars)), int(cannot_be_used_times)
        ):
            clauses.append(tuple([used_vars[i] for i in x]))

    return clauses


def generate_at_most_n_used(poset, linear_extensions_count, expected_ldim, var_getter):
    clauses = []

    cannot_be_used_times = 3
    # for i in range(linear_extensions_count):
    i = 0
    used_vars = [var_getter(VarType.IsUsed, a, i) for a in poset if a & 8 == 0]
    for x in itertools.combinations(range(len(used_vars)), int(cannot_be_used_times)):
        clauses.append(tuple([-used_vars[i] for i in x]))

    return clauses


def all_used(poset, linear_extensions_count, var_getter):
    clauses = []

    for i in range(linear_extensions_count):
        used_vars = [var_getter(VarType.IsUsed, a, i) for a in poset]
        for v in used_vars:
            clauses.append(tuple([v]))

    return clauses


def generate_clauses(dim, linear_extensions_count, local_dim):
    boolean_graph = get_boolean_graph(dim)

    vertices = sorted(boolean_graph.vertices())
    var_getter = construct_variable_map(vertices, linear_extensions_count)

    clauses = generate_poset_clauses(
        boolean_graph, linear_extensions_count, dim, var_getter
    )
    clauses += generate_use_clauses(
        vertices, linear_extensions_count, local_dim, var_getter
    )
    clauses += generate_less_more_clauses(vertices, linear_extensions_count, var_getter)
    clauses += generate_transitivity_clauses(
        vertices, linear_extensions_count, var_getter
    )
    # clauses  += all_used(vertices, linear_extensions_count, var_getter)
    # clauses += generate_at_least_n_used(vertices, linear_extensions_count, local_dim, var_getter)
    # clauses += generate_even_in_ple_clauses(vertices, linear_extensions_count, local_dim, var_getter)
    # clauses += force_from(var_getter, "434.txt", 4, 4, 3)

    # clauses += [tuple([var_getter(VarType.IsUsed, 0, 1)])]
    # clauses += [tuple([var_getter(VarType.IsUsed, 0, 2)])]
    # clauses += [tuple([var_getter(VarType.IsUsed, 0, 3)])]

    # clauses += [tuple([var_getter(VarType.IsUsed, int('111', 2), 1)])]
    # clauses += [tuple([var_getter(VarType.IsUsed, int('111', 2), 2)])]
    # clauses += [tuple([var_getter(VarType.IsUsed, int('111', 2), 3)])]

    # clauses += [tuple([var_getter(VarType.IsUsed, int('110', 2), 0)])]
    # clauses += [tuple([var_getter(VarType.IsUsed, int('101', 2), 0)])]
    # clauses += [tuple([var_getter(VarType.IsUsed, int('011', 2), 0)])]

    # clauses += [tuple([var_getter(VarType.IsUsed, int('101', 2), 1)])]
    # clauses += [tuple([var_getter(VarType.IsUsed, int('101', 2), 3)])]

    # clauses += [tuple([var_getter(VarType.IsUsed, int('010', 2), 2)])]
    # clauses += [tuple([var_getter(VarType.IsUsed, int('010', 2), 3)])]

    # clauses += [tuple([var_getter(VarType.IsUsed, int('001', 2), 1)])]
    # clauses += [tuple([var_getter(VarType.IsUsed, int('001', 2), 3)])]

    # clauses += [tuple([var_getter(VarType.IsLess, int('000', 2), int('001', 2), 0)])]
    # clauses += [tuple([var_getter(VarType.IsLess, int('001', 2), int('010', 2), 0)])]
    # clauses += [tuple([var_getter(VarType.IsLess, int('010', 2), int('100', 2), 0)])]
    # clauses += [tuple([-var_getter(VarType.IsMore, int('011', 2), int('100', 2), 0)])]
    # clauses += [tuple([var_getter(VarType.IsLess, int('011', 2), int('101', 2), 0)])]
    # clauses += [tuple([var_getter(VarType.IsLess, int('101', 2), int('110', 2), 0)])]
    # clauses += [tuple([var_getter(VarType.IsLess, int('110', 2), int('111', 2), 0)])]

    # for v in vertices:
    #     clauses += [tuple([var_getter(VarType.IsUsed, v, 0)])]

    # clauses_x = []
    # for v in vertices:
    #     for u in vertices:
    #         if v < u and int(v).bit_count() < int(u).bit_count():
    #             clauses_x.append(tuple([var_getter(VarType.IsLess, v, u, 0)]))
    #             clauses_x.append(tuple([-var_getter(VarType.IsMore, v, u, 0)]))
    # clauses += clauses_x

    return clauses


def save_problem(dim, local_dim, linear_extensions_count, file_name):
    clauses = generate_clauses(dim, linear_extensions_count, local_dim)

    sat_generator = DIMACS()
    for c in clauses:
        sat_generator.add_clause(c)
    sat_generator.clauses(file_name)


if __name__ == "__main__":
    save_problem(
        dim=6,
        local_dim=3,
        linear_extensions_count=5,
        file_name="dim.dimacs",
    )
