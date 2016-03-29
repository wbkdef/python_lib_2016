__author__ = 'Willem'

import math
import operator
import random
from typing import Iterable
import textwrap

import numpy as np
from sklearn.ensemble import RandomForestClassifier


# ------------ MACHINE LEARNING - General Fcns -------------------
def summarize_by_random_sample(num, dict_list_or_set):
    """Returns a sorted list (by value in the case of dicts)

    of num randomly sampled elements"""
    num = min(num, len(dict_list_or_set))
    l = random.sample(dict_list_or_set, num)
    if isinstance(dict_list_or_set, dict):
        d = dict_list_or_set
        l = [(k, d[k]) for k in l]
        l.sort(key=operator.itemgetter(1))
    else:
        l.sort()
    return l


def take_exp_of_dict_values_and_normalize(dict_):
    """dict_ is a dictionary of labels and values

    This function takes the exponential of each of the values
    and normalizes by the sum of the exponentials to get the
    probability of each label"""
    m = max(dict_.values())  # For log sum trick
    probs = {l: math.exp(v - m) for l, v in dict_.iteritems()}
    s = sum(probs.values())
    for l in probs:
        probs[l] /= s
    return probs


def random_round(
        num):  # How to round to an integer randomly, so that the expected value is the number?
    return int(num) + (random.random() < num % 1)


def error_rate(Y1, Y2,
               num_decimals=None):  # How to get the error rate given actual and predicted labels?
    assert len(Y1) == len(Y2)

    error_rate = sum([1 for y1, y2 in zip(Y1, Y2) if y1 != y2]) / len(Y1)
    if num_decimals is not None:
        error_rate = round(error_rate, num_decimals)
    return error_rate


# ------------ MACHINE LEARNING - Dicts of Feats -------------------
def get_all_features(list_of_sets_of_features, show_pulse=True):  # How to get the
    all_feats = set([])
    if show_pulse: print
    "Generating set of all features from ", int(
        len(list_of_sets_of_features) / 1000), "thousand sets"
    for i in range(len(list_of_sets_of_features)):
        feats = list_of_sets_of_features[i]
        all_feats.update(feats)
        if show_pulse and i % 1000 == 0:
            print
            int(i / 1000),
    if show_pulse: print
    "Done Generating Features"
    return all_feats


def create_synthetic_data(num_labels, num_feats, num_train_labelled, num_unlabelled, num_test,
                          sparsity=3, skew=2, rand_seed=None):  # How to get the
    """Returns Synthetic Data in a dictionary with keys:
       "X_train", "y_train", "X_unlabelled", "X_test", "y_test" """
    import random
    # results=[X_train,y_train,X_unlabelled,X_test,y_test]
    assert num_feats <= 26
    feats = set('abcdefghijklmnopqrstuvwxyz'[:num_feats])
    labels = range(1, num_labels + 1)
    assert sparsity >= skew
    if rand_seed != None:
        random.seed(rand_seed)

    feat_probs = {}
    for f in feats:
        feat_probs[f] = random.random() ** (sparsity - skew)
    feat_label_probs = {l: {} for l in labels}
    for l in labels:
        for f in feats:
            feat_label_probs[l][f] = random.random() ** skew * feat_probs[f]

    def generate_X_Y(n):
        Y = [random.randint(1, num_labels) for x in range(n)]
        X = []
        for i in range(n):
            X.append(set())
            for f in feats:
                if random.random() < feat_label_probs[Y[i]][f]:
                    X[-1].add(f)
        return X, Y

    data = {}
    data["X_train"], data["y_train"] = generate_X_Y(num_train_labelled)
    data["X_unlabelled"], y = generate_X_Y(num_unlabelled)
    data["X_test"], data["y_test"] = generate_X_Y(num_train_labelled)

    return data


def gen_corrupted_features1(x, d):  # How to get the
    """This is called by gen_corrupted_features to corrupt the features of a single example"""
    return set(random.sample(x, random_round((1 - d) * len(x))))


def gen_corrupted_features(X, Y, d, num_corruptions_per_point):  # How to get the
    assert (d >= 0 and d < 1)
    new_X = []
    new_Y = []
    for i in range(int(num_corruptions * len(X))):
        n = random.randint(0, len(X))
        new_X.append(gen_corrupted_features1(X[n], d))
        new_Y.append(Y[n])
    return new_X, new_Y




# Numpy and Scikit Learn -----------------------------------------------

def split_train_cross_val(X_maybe_y:Iterable[np.ndarray], frac_train=.75, replace=False):
    _assert_they_all_have_same_num_rows(X_maybe_y)
    cross_validate, train = _generate_train_and_cv_row_indices(len(X_maybe_y[0]), frac_train)
    split_data = [array[train] for array in X_maybe_y] +\
                 [array[cross_validate] for array in X_maybe_y]
    return split_data


def _assert_they_all_have_same_num_rows(args):
    assert len(set([arg.shape[0] for arg in args])) == 1


def _generate_train_and_cv_row_indices(num_rows: int, frac_train:float):
    # num_rows = args[0].shape[0]
    num_train = math.floor(num_rows * frac_train)
    train = np.random.choice(num_rows, size=num_train, replace=False)
    train_set = set(train)
    cross_validate = [i for i in range(num_rows) if i not in train_set]
    return cross_validate, train

# __Q:  Create this function! todo_2016_03_07 todo_2016_03_14 todo_2016_04_04 todo_2016_06_06 todo_2017_02_06 todo_2019_07_08 todo_2026_04_06
def deliberative_practice_generate_train_and_cv_row_indices(num_rows: int, frac_train:float):

    return cv_ind, train_ind


class CrossValidationResults:
    def __init__(self,
                 results,
                 frac_train=.75,
                 randomized=True,
                 replace=False):
        self.frac_train = frac_train
        self.randomized = randomized
        self.num_trainings = len(results)
        self.replace = replace
        self.results = results
        self.mean = sum(results)/len(results)

    def __str__(self):
        s = ""
        s += "frac_train = %s" % self.frac_train
        s += "\nrandomized = %s" % self.randomized
        s += "\nnum_trainings = %s" % self.num_trainings
        s += "\nreplace = %s" % self.replace
        s += "\nresults = %s" % self.results
        s += "\nmean = %s" % self.mean
        textwrap.indent(s, "    ")
        s = "CrossValidationResults:\n" + s
        return s

    @property
    def mean_std_err(self):
        raise NotImplementedError()


def do_cross_validation(sklearn_classifiers:Iterable[RandomForestClassifier],
                        feats:np.ndarray,
                        labels:np.ndarray,
                        frac_train=.75,
                        randomized=True,
                        replace=False) -> CrossValidationResults:
    assert randomized, "Non-random (i.e. 5-fold) cross-validation not implemented yet"
    results = []
    for classifier in sklearn_classifiers:
        feats_train, labels_train, feats_cv, labels_cv = \
            split_train_cross_val([feats, labels], frac_train, replace)
        classifier.fit(feats_train, labels_train)
        pred = classifier.predict(feats_cv)
        err = error_rate(pred, labels_cv)
        results.append(err)
    cv_results = CrossValidationResults(results, frac_train, randomized, replace)
    return cv_results


def  deliberate_practice_do_cross_validation(sklearn_classifiers:Iterable[RandomForestClassifier],
                        feats:np.ndarray,
                        labels:np.ndarray,
                        frac_train=.75,
                        randomized=True,
                        replace=False) -> CrossValidationResults:
    assert randomized, "Non-random (i.e. 5-fold) cross-validation not implemented yet"
    results = []
    for classifier in sklearn_classifiers:
        feats_train, labels_train, feats_cv, labels_cv = \
            split_train_cross_val([feats, labels], frac_train, replace)
        # __A:
        classifier.fit(feats_train, labels_train)
        pred = classifier.predict(feats_cv)
        err = error_rate(pred, labels_cv)
        # __Q:  Train the classifier and determine the error on the cv data! todo_2016_03_07 todo_2016_03_14 todo_2016_04_04 todo_2016_06_06 todo_2017_02_06 todo_2019_07_08 todo_2026_04_06

        results.append(err)
    cv_results = CrossValidationResults(results, frac_train, randomized, replace)
    return cv_results

