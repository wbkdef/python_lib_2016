# import os
from textwrap import indent

import misc_lib as ml

def test_get_path_to_file_in_this_modules_directory():
    file_name = 'fn'
    file_path = r'C:\Users\Willem\Desktop\organization\Code_To_Keep\python\tests\fn'
    assert ml.get_path_to_file_in_this_modules_directory(__file__, file_name) == file_path

# __c I don't know why I get the following error!   PermissionError: [Errno 13] Permission denied: 'x_pkl'
# def test_pickle_unpickle():
#     x = [3, 5, 8]
#     # filename = "x.pickle"
#     filename = "x_pkl"
#     ml.pickle_to_filename(x, filename)
#     y = ml.unpickle_from_filename(filename)
#     assert x == y

def test_dicts_almost_equal():
    assert ml.dicts_almost_equal(5, 5)
    assert ml.dicts_almost_equal({1:3, 5:4/3}, {1:3, 5:1.33333333333333333})
    assert ml.dicts_almost_equal({1:{2:5, 7:1}, 5:4/3}, {1:{2:5, 7:1}, 5:1.33333333333333333})

# def test_indent():
#     s = "This is a \npretty cool\nstring!"
#     assert ml.indent(s) == "\tThis is a \n\tpretty cool\n\tstring!"
#     assert ml.indent(s, indent_first_line=True) == "\tThis is a \n\tpretty cool\n\tstring!"
#     assert ml.indent(s, indent_first_line=False) == "This is a \n\tpretty cool\n\tstring!"
#     assert ml.indent(s, "  ") == "  This is a \n  pretty cool\n  string!"
#     assert ml.indent(s, "  ", indent_first_line=True) == "  This is a \n  pretty cool\n  string!"
#     assert ml.indent(s, "  ", indent_first_line=False) == "This is a \n  pretty cool\n  string!"


def test_indent():
    s = "This is a \npretty cool\nstring!"
    assert indent(s, "\t") == "\tThis is a \n\tpretty cool\n\tstring!"
    assert indent(s, "  ") == "  This is a \n  pretty cool\n  string!"


def test_abbreviate_python_var_or_title():
    assert ml.abbreviate_python_var_or_title('my_expression 12') == 'me12'
    assert ml.abbreviate_python_var_or_title('my_exprESsion 12') == 'meES12'


