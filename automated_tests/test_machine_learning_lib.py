
import numpy as np
from machine_learning_lib import split_train_cross_val

def test_split_train_cross_val():
    rng = np.arange(9)
    train, cv = split_train_cross_val(rng, frac_train=.75, replace=False)
    assert len(train) == 6
    assert len(cv) == 3

    assert set(range(9)) == set(train) | set(cv)

    # assert 0, "%s %s"%(train, cv)


