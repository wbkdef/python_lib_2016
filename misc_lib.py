import os
import math
import re

import pickle


def get_date_time_string():  #How to get the date and time as a string (suitable for use in file names)?
  import datetime
  return str(datetime.datetime.now())[5:19].replace(":",",").replace(" ","_")

def beeps(n):  #How to make the computer beep (i.e. when a program is finished running)?
  import time
  import winsound
  for i in range(n):
    winsound.MessageBeep()
    time.sleep(1)

# Reminder Have This function! todo_2016_11_07 todo_2019_06_03 todo_2026_02_02
def get_path_to_file_in_this_modules_directory(modules__file__, filename):
    abs_path = os.path.realpath(modules__file__)
    dir_name = os.path.dirname(abs_path)
    file_path = os.path.join(dir_name, filename)
    return file_path

def unpickle_from_filename(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def pickle_to_filename(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def pickle_caching(fcn):
    def wrapper(filename):
        pickle_filename = filename + ".pickle"
        if os.path.isfile(pickle_filename):
            return unpickle_from_filename(pickle_filename)
        else:
            obj = fcn(filename)
            pickle_to_filename(obj, pickle_filename)
            assert os.path.isfile(pickle_filename)
            return obj
    return wrapper

# pickle_to_filename("hello", "my_pkl")

def almost_equal(A, B, rel_threshold=0.000001):
    abs_threshold = math.fabs(A*rel_threshold)
    return math.fabs(A-B) <= abs_threshold

def dicts_almost_equal(a, b, rel_threshold=0.000001):
    try:
        a_keys, b_keys = a.keys(), b.keys()
    except AttributeError:
        return almost_equal(a, b, rel_threshold)
    if a_keys != b_keys:
        return False
    for key in a:
        if not dicts_almost_equal(a[key], b[key], rel_threshold):
            return False
    return True

## __c Use textwrap.indent instead!
# def indent(str_, padding='\t', indent_first_line=True):
#     indented = ('\n'+padding).join(str_.split('\n'))
#     if indent_first_line:
#         indented = padding + indented
#     return indented

e = re.compile(r'((?<![a-zA-Z])[a-z]|[A-Z0-9])')
def abbreviate_python_var_or_title(s):
    m = e.findall(s)
    abb = ''.join(m)
    return abb


































