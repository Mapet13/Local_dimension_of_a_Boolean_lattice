import random
import copy
import sys
from typing import Optional
from itertools import filterfalse, combinations

from singletons_fixtures import From_sat_636

from boolean_lattice_utils import (
    elements_gen,
    is_singleton,
    singletons_gen_n,
    not_singletons_gen,
    is_subset,
    to_string,
    count_elements,
    pairs_gen,
    Realizer,
    Ple,
)


def is_correct_placement(n: int, element: int, realizer: Realizer) -> bool:
    in_elm = lambda sin: is_subset(sin, element) or element == 0
    comperable = {x: False for x in filter(in_elm, singletons_gen_n(n))}
    incomperable = {x: [False, False] for x in filterfalse(in_elm, singletons_gen_n(n))}

    has_element = lambda ple: element in ple
    for ple in filter(has_element, realizer):
        is_lower = True
        for x in ple:
            if x == element:
                is_lower = False
            elif x in comperable and not is_lower:
                return False
                # if is_lower:
                #    comperable[x] = True
                # else:
                #    return False
            elif x in incomperable:
                incomperable[x][int(is_lower)] = True

    # return all(comperable.values()) and all(map(all, incomperable.values()))
    found_above = [x[0] for x in incomperable.values()]
    return all(found_above)


def get_next_singleton(ple: Ple, start: int = 0) -> Optional[int]:
    for idx in range(start, len(ple)):
        if is_singleton(ple[idx]):
            # print(start, ple, idx)
            return idx
    return None


def get_ple_choices(n: int, realizer: Realizer) -> list[tuple[int, ...]]:
    # TODO: optimize (remove choices that not contains all singletons)
    to_select = len(realizer)
    return list(combinations(range(to_select), n))


def try_fill_realizer_with(
    element: int, n: int, width: int, singletons_realizer: Realizer
) -> Optional[Realizer]:

    # TODO: that could be done once, before that function
    ple_choices = get_ple_choices(width, singletons_realizer)

    def get_next_indices(indices: list[int], ples: Realizer) -> Optional[list[int]]:
        for i in reversed(range(width)):
            new_idx = get_next_singleton(ples[i], indices[i])
            if new_idx is not None:
                indices[i] = new_idx + 1
                return indices
            else:
                indices[i] = 0

        return None

    for ple_selection in ple_choices:
        ples = [singletons_realizer[i] for i in ple_selection]

        idx_tracker = [0] * width
        while idx_tracker is not None:
            new_realizer = copy.deepcopy(singletons_realizer)
            for ple_idx, insert_idx in enumerate(idx_tracker):
                new_realizer[ple_selection[ple_idx]].insert(insert_idx, element)
            if is_correct_placement(n, element, new_realizer):
                # print(f"found placement for {element} - {new_realizer}")
                return new_realizer
            idx_tracker = get_next_indices(idx_tracker, ples)

    print(f"Cannot find placement for {to_string(element, n, should_center = False)}")
    return None


def try_fill_realizer(n: int, width: int, realizer: Realizer) -> Optional[Realizer]:
    fill_with = lambda x: try_fill_realizer_with(x, n, width, copy.deepcopy(realizer))
    with_single_inserted = list(map(fill_with, elements_gen(n)))

    # return with_single_inserted[3]

    is_none = lambda x: x is None
    if any(map(is_none, with_single_inserted)):
        return None

    # with_single_inserted = [with_single_inserted[3]]

    # TODO:  tu sie cos psuje :c
    result = copy.deepcopy(realizer)
    for realizer_with_element in with_single_inserted:
        assert realizer_with_element is not None
        for result_ple, element_ple in zip(result, realizer_with_element):
            insert_idx = get_next_singleton(result_ple, 0)
            for element in element_ple:
                if is_singleton(element):
                    assert insert_idx is not None
                    insert_idx = get_next_singleton(result_ple, insert_idx + 1)
                    # print(insert_idx)
                    if insert_idx is None:
                        insert_idx = len(result_ple)
                    # else:
                    # insert_idx += 1
                else:
                    # print(result_ple, insert_idx, element)
                    result_ple.insert(insert_idx, element)

    return result


def count_in_realizer(element: int, realizer: Realizer) -> int:
    counter = 0
    for ple in realizer:
        for x in ple:
            if x == element:
                counter += 1
    return counter


def can_select_ple_for_inc_for_pairs(n: int, width: int, srealizer: Realizer) -> bool:
    singletons = list(singletons_gen_n(n))
    ple_choices = get_ple_choices(width, srealizer)
    for to_check in combinations(singletons, n - 2):
        found_any = False
        for ple_selection in ple_choices:
            ples = [srealizer[i] for i in ple_selection]
            occures_twice = lambda s: count_in_realizer(s, ples) >= 2
            if all(map(occures_twice, to_check)):
                found_any = True
                break
        if not found_any:
            return False
    return True


def find_minimal_insert_places(element: int, srealizer: Realizer) -> list[int]:
    result = [len(ple) - 1 for ple in srealizer]

    for ple_idx in range(len(srealizer)):
        for s in reversed(srealizer[ple_idx]):
            if is_subset(s, element):
                break
            result[ple_idx] -= 1

    return result


def can_find_all_incomperable_above_singletons_for(
    element: int, n: int, width: int, srealizer: Realizer
) -> bool:
    in_elm = lambda sin: is_subset(sin, element) or element == 0
    incomperable = list(filterfalse(in_elm, singletons_gen_n(n)))

    ple_choices = get_ple_choices(width, srealizer)
    insert_places = find_minimal_insert_places(element, srealizer)
    for ple_selection in ple_choices:
        find_incomperable = {s: False for s in incomperable}
        for ple_idx in ple_selection:
            for elem_idx in range(insert_places[ple_idx] + 1, len(srealizer[ple_idx])):
                find_incomperable[srealizer[ple_idx][elem_idx]] = True
        if all(find_incomperable.values()):
            return True

    return False


def can_find_all_incomperable_above_singletons(
    n: int, width: int, srealizer: Realizer
) -> bool:
    check_element = lambda x: can_find_all_incomperable_above_singletons_for(
        x, n, width, srealizer
    )
    return all(map(check_element, pairs_gen(n)))


def get_random_singletons_distr(n: int, width: int, ple_count: int) -> Realizer:
    result = [[] for _ in range(ple_count)]

    for singleton in singletons_gen_n(n):
        for ple_idx in random.sample(range(ple_count), width):
            result[ple_idx].append(singleton)

    for ple_idx in range(ple_count):
        random.shuffle(result[ple_idx])

    return result


def get_random_singletons_distr_uniq_top(
    n: int, width: int, ple_count: int
) -> Realizer:
    result = [[] for _ in range(ple_count)]

    for sidx, singleton in enumerate(singletons_gen_n(n)):
        for ple_idx in random.sample(range(ple_count - 1), width - 1):
            if ple_idx >= sidx:
                ple_idx += 1
            result[ple_idx].append(singleton)

    for ple_idx in range(ple_count):
        random.shuffle(result[ple_idx])

    for sidx, singleton in enumerate(singletons_gen_n(n)):
        result[sidx].append(singleton)

    return result


def get_offset_singletons_distr(n: int, width: int, ple_count: int) -> Realizer:
    result = [[] for _ in range(ple_count)]

    for offset in reversed(range(width)):
        for sidx, singleton in enumerate(singletons_gen_n(n)):
            result[(sidx + offset) % ple_count].append(singleton)

    result[1].remove(1)
    result[2].remove(2)
    result = result + [[1, 2]]

    return result


def try_with_random(n: int, width: int, ple_count: int) -> bool:
    distr = get_random_singletons_distr_uniq_top(n, width, ple_count)

    def is_correct(srealizer: Realizer) -> bool:
        return can_select_ple_for_inc_for_pairs(
            n, width, srealizer
        ) and can_find_all_incomperable_above_singletons(n, width, srealizer)

    while not is_correct(distr):
        distr = get_random_singletons_distr_uniq_top(n, width, ple_count)

    realizer = try_fill_realizer(n, width, distr)
    return realizer is not None


def get_ranmdom_stats(runs: int, n: int, width: int, ple_count: int) -> tuple[int, int]:
    found = 0
    not_found = 0

    for i in range(runs):
        print(f"{i}/{runs}")
        if try_with_random(n, width, ple_count):
            found += 1
        else:
            not_found += 1

    return (found, not_found)


def find_636_from_sat() -> Optional[Realizer]:
    n = From_sat_636.N
    width = From_sat_636.WIDTH
    singletons = [list(filter(is_singleton, ple)) for ple in From_sat_636.REALIZER]
    return try_fill_realizer(n, width, singletons)


if __name__ == "__main__":
    # r = find_636_from_sat()
    # print(r)
    # sys.exit(0)

    n = 8
    width = 3
    ple_count = 8

    # distr = get_random_singletons_distr_uniq_top(n, width, ple_count)
    distr = get_offset_singletons_distr(n, width, ple_count)

    def is_correct(srealizer: Realizer) -> bool:
        # return can_select_ple_for_inc_for_pairs(
        #   n, width, srealizer
        # ) and
        return can_find_all_incomperable_above_singletons(n, width, srealizer)

        # while not is_correct(distr):
        # distr = get_random_singletons_distr_uniq_top(n, width, ple_count)

    to_str = lambda x: to_string(x, n, should_center=False)

    for ple in distr:
        print(list(map(to_str, ple)))
    print("----")

    realizer = try_fill_realizer(n, width, distr)
    if realizer is None:
        print("! Cannot fill realizer !")
    else:
        print(realizer)

    # to_str = lambda x: to_string(x, n, should_center=True)

    # if realizer is not None:
    # for ple in realizer:
    #    print(list(map(to_str, ple)))
    # print("----")

    # runs = 20
    # found, not_found = get_ranmdom_stats(runs, n, width, ple_count)
    # print(f"found = {found}")
    # print(f"not found = {not_found}")
