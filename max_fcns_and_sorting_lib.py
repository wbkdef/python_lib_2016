__author__ = 'Willem'

import operator
import random
import logging

def identity(x): return x


# ------------------------ Max Fcns and Sorting -----------------------------

def get_iterable_of_arg_val_tuples(data : "Sequence or dict",
                                   key=None):
    if isinstance(data, (list, tuple)):
        iterable = enumerate(data)
    elif isinstance(data, dict):
        iterable = data.items()
    else:
        logging.critical("Data type not recognized")
        logging.critical(data)
        assert False

    if key is None:
        key = identity
    list_ = [(k, key(value)) for k, value in iterable]
    return list_

# OLD FCNS
# def max_n_or_more_arg_val_tuples(data_, n, key=None):
#     """Returns a list of the top n indices/keys of list/dict data_
#
#     key is a function applied to the values before sorting
#     If there is a tie for the nth largest item, all tiying items are
#     returned
#     """
#     iterable = get_iterable_of_arg_val_tuples(data_, key)
#     list_ = sorted(iterable, key=operator.itemgetter(1), reverse=True)
#     last_val = list_[n - 1]
#     j = n - 1
#     while (list_[j] >= last_val):
#         j += 1
#     return list_[:j]


# def max_n_arg_val_tuples(data_, n, key=None, random_tie_breaking=True):
#     """Returns a list of the top n indices/keys of list/dict data_
#
#     key is a function applied to the values before sorting
#     """
#     list_ = max_n_or_more_arg_val_tuples(data_, n, key, random_tie_breaking)
#     if not random_tie_breaking or len(list_) == n:
#         return list_[:n]
#     else:
#         i = n - 1
#         while (list_[i - 1] <= last_val):
#             i -= 1
#         solutions = list_[:i] + random.sample(n - i, list_[i:])
#         return solutions

def max_arg_val_dict(data_ : "Sequence or Dict",
                     key=None):
    """Returns a dict of arg:val items for which val is max(key(values))"""
    assert len(data_) >= 1, data_
    if key is None:
        key = identity
    fcn = lambda x: key(operator.itemgetter(1)(x))
    iterable = get_iterable_of_arg_val_tuples(data_)
    m = max(iterable, key=fcn)[1]
    max_dict = {k : v for k, v in iterable if key(v) == key(m)}
    return max_dict

def _choose(list_, random_tie_breaking=True, None_if_tie=False):
    if len(list_) == 1:
        return list_[0]
    elif len(list_) > 1:
        if None_if_tie:
            return None
        return random.choice(list_)
    else:
        assert False, list_

def max_arg_val_tuple(data_, random_tie_breaking=True, key=None, None_if_tie=False):
    """Returns an (arg, val) tuple for which val is max(vals)

    key is a function applied to the values before maximizing"""
    max_dict = max_arg_val_dict(data_, key)
    max_tuples = list(max_dict.items())
    return _choose(max_tuples, random_tie_breaking, None_if_tie)

def _argmax(data_, key=None, None_if_tie=False, random_tie_breaking=True):
    max_dict = max_arg_val_dict(data_, key)
    max_args = list(max_dict.keys())
    return _choose(max_args, random_tie_breaking, None_if_tie)

# __c deterministic tie breaking still isn't the same each time, so decided to always make it random.
# def argmax_deterministic_tie_breaking(data_, key=None):return _argmax(data_, key, False)
def argmax_random_tie_breaking(data_, key=None):return _argmax(data_, key)
def argmax_None_if_tie(data_, key=None):return _argmax(data_, key, True)


def sorted_args(data_, key=None, reverse=False): pass
