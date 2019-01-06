import time


def timer(func):
    def timed_func(*args, **kwargs):
        before = time.time()
        return_value = func(*args, **kwargs)
        after = time.time()
        total = after - before
        print(func.__name__ + "() elapsed:", total, "seconds")
        return return_value, total
    timed_func.__name__ = func.__name__
    return timed_func
