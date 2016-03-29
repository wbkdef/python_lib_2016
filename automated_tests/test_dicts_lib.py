
import pytest as pt
from collections import  defaultdict

from dicts_lib import dict_add_dict_to, dict_sum_values, default_dicts_to_common_dict_recursively


@pt.fixture()
def d():
    return {1:3, 4:8}

@pt.fixture()
def default_d():
    d = defaultdict(int)
    d[2] = 5
    d[4] = 7
    d[7]
    return d

@pt.fixture()
def d_added(d, default_d):
    dict_add_dict_to(d, default_d)
    return d

def test_dict_add_dict_to(d_added, d, default_d):
    assert d_added == {1:3, 2:5, 4:15, 7:0}
    assert d == {1:3, 2:5, 4:15, 7:0}
    assert default_d == {2:5, 4:7, 7:0}

def test_dict_sum_values(d, default_d):
    assert dict_sum_values(d, d.keys()) == 11
    assert dict_sum_values(d, [4]) == 8
    assert dict_sum_values(default_d, default_d.keys()) == 12
    assert dict_sum_values(default_d, {4, 7}) == 7

def test_default_dicts_to_common_dict_recursively(default_d, d):
    x = 5
    assert default_dicts_to_common_dict_recursively(x) == x

    cd = default_dicts_to_common_dict_recursively(default_d)
    assert cd == {2:5, 4:7, 7:0}
    assert isinstance(cd, dict)
    assert not isinstance(cd, defaultdict)

    assert default_dicts_to_common_dict_recursively(d) == d

    default_d[6] = defaultdict(float)
    default_d[6][4]+=3
    cd = default_dicts_to_common_dict_recursively(default_d)
    assert cd == {2:5, 4:7, 7:0, 6:{4:3}}
    assert isinstance(cd, dict)
    assert isinstance(cd, dict)
    assert not isinstance(cd, defaultdict)
    assert not isinstance(cd, defaultdict)

