from functools import wraps
from flexible_logger import log
from typing import Callable

def _apply_processing(arg, fcn_or_dict):
    try:
        return fcn_or_dict(arg)
    except Exception:
        return fcn_or_dict[arg]

def pre_process_inputs(*args, **kwargs):
    def new_fcn_getter(fcn):
        @wraps(fcn)
        def new_fcn(*args2, **kwargs2):
            args2 = list(args2)
            for i, f in enumerate(args):
                args2[i] = _apply_processing(args2[i], f)
            for key, f in kwargs.items():
                kwargs2[key] = _apply_processing(kwargs2[key], f)
            return fcn(*args2, **kwargs2)
        return new_fcn
    return new_fcn_getter

def post_process_outputs():
    pass

def log_fcn_in_out(priority, log_in_out=True, log_in=False):
    def decorator(fcn: Callable):
        @wraps(fcn)
        def logged_fcn(*args, **kwargs):
            in_args = "\ninto fcn: " + fcn.__name__ + \
                      "\n\targs: " + str(args) + \
                      "\n\tkwargs: " + str(kwargs)
            if log_in:
                log(in_args, priority)
            res = fcn(*args, **kwargs)
            in_out = in_args + "\nres: " + str(res)
                    # "\n\nout of fcn: " + fcn.__name__ + \
            if log_in_out:
                log(in_out, priority)
            return res
        return logged_fcn
    return decorator
    # This should use the logging file set up!  Log what comes in and what goes out!