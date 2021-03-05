"""Build the timefunc decorator."""

import time
import functools


def timefunc(func):
    """timefunc's doc"""
    @functools.wraps(func)
    def time_closure(*args, **kwargs):
        """time_wrapper's doc string"""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - start
        print(f"Function: {func.__name__}, Time: {time_elapsed}")
        return result

    return time_closure

@timefunc
def test():
    return [i for i in range(0, 1000000)]

if __name__ == "__main__":
    test()
