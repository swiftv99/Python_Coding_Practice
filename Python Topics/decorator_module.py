import functools
import time

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        # Do something
        result = func(*args, **kwargs)
        # Do something
        return result
    return wrapper_do_twice


def timer(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        # Do something
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        # Do something
        t2 = time.perf_counter()
        print(f"Finished {func.__name__!r} in {t2-t1: 4f} secs")
        return result
    return wrapper_do_twice
