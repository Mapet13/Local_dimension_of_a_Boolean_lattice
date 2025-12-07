from gen_singletons import (
    try_fill_realizer,
    is_correct_placement,
    can_select_ple_for_inc_for_pairs,
    can_find_all_incomperable_above_singletons,
)
from boolean_lattice_utils import is_singleton
from singletons_fixtures import From_sat_636


def test_is_correct_placement_for_0():
    placement = [
        [4, 1, 0],
        [8, 16, 32, 0],
        [1, 2, 0],
        [32, 4],
        [4, 32, 1, 16, 2, 8],
        [8, 2, 16],
    ]

    assert is_correct_placement(6, 0, placement)


def test_find_from_sat():
    n = From_sat_636.N
    width = From_sat_636.WIDTH

    singletons = [list(filter(is_singleton, ple)) for ple in From_sat_636.REALIZER]

    assert can_find_all_incomperable_above_singletons(n, width, singletons)
    assert can_select_ple_for_inc_for_pairs(n, width, singletons)
    assert try_fill_realizer(n, width, singletons) is not None
