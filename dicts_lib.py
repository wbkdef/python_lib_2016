__author__ = 'Willem'


def dict_add_dict_to(d, dict_to_add):  # How to add the values of one dictionary to another?
    """Modifies d so that
    1) If a key originally occurs in only one of 'd' and 'dict_to_add'
    then that will be the value in d for that key.
    2) If a key originally occurs in both 'd' and 'dict_to_add'
    then the final value for key in d will be the sum of the values
    from both dictionaries"""
    for key, value in dict_to_add.items():
        if key not in d:
            d[key] = value
        else:
            d[key] += value

def dict_sum_values(my_dict, keys):  # How to get the
    return sum([my_dict[key] for key in keys if key in my_dict])

def default_dicts_to_common_dict_recursively(dict_):
    try:
        items = dict_.items()
    except AttributeError:
        return dict_ #It's not a dict

    return {key:default_dicts_to_common_dict_recursively(val) for key, val in items}

# def dicts_almost_equal():pass
#     See misc_lib
