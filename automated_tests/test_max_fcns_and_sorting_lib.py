import operator

import pytest

__author__ = 'Willem'

from max_fcns_and_sorting_lib import get_iterable_of_arg_val_tuples, max_arg_val_dict, max_arg_val_tuple, argmax_random_tie_breaking, \
    argmax_None_if_tie


def test_get_iterable_of_arg_val_tuples():
    assert list(get_iterable_of_arg_val_tuples([1, 5, 3, 9])) == [(0, 1), (1, 5), (2, 3), (3, 9)]
    assert list(get_iterable_of_arg_val_tuples({1:5, 3:9})) in ([(1, 5), (3, 9)], [(3, 9), (1, 5)])

def test_max_arg_val_tuples():
    assert max_arg_val_dict([1, 5, 3, 9]) == {3:9}
    assert max_arg_val_dict([9, 5, 11, 2, 11]) == {2:11, 4:11}
    assert max_arg_val_dict({1:5, 3:9}) == {3:9}

    assert max_arg_val_dict([(0, 1), (1, 5), (2, 3), (3, 9), (4, 7)]) == {4:(4, 7)}
    assert max_arg_val_dict([(0, 1), (1, 5), (2, 3), (3, 9), (4, 7)], key=operator.itemgetter(1)) == {3:(3, 9)}

def test_max_arg_val_tuple():
    assert max_arg_val_tuple([1, 5, 3, 9]) in [(3, 9)]
    assert max_arg_val_tuple([9, 5, 11, 2, 11]) in [(2, 11), (4, 11)]
    assert max_arg_val_tuple({1:5, 3:9}) in [(3, 9)]
    assert max_arg_val_tuple([(0, 1), (1, 5), (2, 3), (3, 9), (4, 7)]) in [(4, (4, 7))]
    assert max_arg_val_tuple([(0, 1), (1, 5), (2, 3), (3, 9), (4, 7)], key=operator.itemgetter(1)) in [(3, (3, 9))]

@pytest.mark.parametrize("fcn", [argmax_random_tie_breaking, argmax_None_if_tie])
def test_argmax_fcns_when_no_tie(fcn):
    assert fcn([1, 5, 3, 9]) == 3
    assert fcn({1:5, 3:9}) == 3
    assert fcn([(0, 1), (1, 5), (2, 3), (3, 9), (4, 7)]) == 4
    assert fcn([(0, 1), (1, 5), (2, 3), (3, 9), (4, 7)], key=operator.itemgetter(1)) == 3

def get_set_of_results(fcn, arg, times = 50):
    # return [fcn(arg) for i in range(times)]
    return {fcn(arg) for i in range(times)}

def test_argmax_fcns_when_there_is_a_tie():
    rr = get_set_of_results(argmax_random_tie_breaking, [9, 5, 11, 2, 11])
    nr = get_set_of_results(argmax_None_if_tie, [9, 5, 11, 2, 11])
    assert rr == {2, 4}
    assert nr == {None}
    # assert len(dr) == 1
    # assert len(rr) == 2



# def test_argmax_deterministic_tie_breaking():
#     assert argmax_deterministic_tie_breaking([1, 5, 3, 9]) in [3]
#     assert argmax_deterministic_tie_breaking([9, 5, 11, 2, 11]) in [2, 4]
#     assert argmax_deterministic_tie_breaking({1:5, 3:9}) in [3]
#     assert argmax_deterministic_tie_breaking([(0, 1), (1, 5), (2, 3), (3, 9), (4, 7)]) in [4]
#     assert argmax_deterministic_tie_breaking([(0, 1), (1, 5), (2, 3), (3, 9), (4, 7)], key=operator.itemgetter(1)) in [3]
#
# def test_argmax_random_tie_breaking():
#     assert argmax_random_tie_breaking([1, 5, 3, 9]) in [3]
#     assert argmax_random_tie_breaking([9, 5, 11, 2, 11]) in [2, 4]
#     assert argmax_random_tie_breaking({1:5, 3:9}) in [3]
#     assert argmax_random_tie_breaking([(0, 1), (1, 5), (2, 3), (3, 9), (4, 7)]) in [4]
#     assert argmax_random_tie_breaking([(0, 1), (1, 5), (2, 3), (3, 9), (4, 7)], key=operator.itemgetter(1)) in [3]
# def test_argmax_None_if_tie():
#     assert argmax_None_if_tie([1, 5, 3, 9]) in [3]
#     assert argmax_None_if_tie([9, 5, 11, 2, 11]) in [2, 4]
#     assert argmax_None_if_tie({1:5, 3:9}) in [3]
#     assert argmax_None_if_tie([(0, 1), (1, 5), (2, 3), (3, 9), (4, 7)]) in [4]
#     assert argmax_None_if_tie([(0, 1), (1, 5), (2, 3), (3, 9), (4, 7)], key=operator.itemgetter(1)) in [3]




