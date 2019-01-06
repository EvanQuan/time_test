import math
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


pow_count = 10_000_000


@timer
def timepow():
    for i in range(pow_count):
        num = i**0.5


@timer
def timesqrt():
    for i in range(pow_count):
        num = math.sqrt(i)


map_count = 10_000_000


@timer
def timemap():
    list(map(str, range(map_count)))


@timer
def timelistcomp():
    [str(i) for i in range(map_count)]


def main():
    empty, t_pow = timepow()
    empty, t_sqrt = timesqrt()
    emtpy, t_map = timemap()
    emtpy, t_list = timelistcomp()

    print()
    print("sqrt(i) is %.2f%% faster than **0.5 for count of %i" % (t_pow / t_sqrt * 100 - 100, pow_count))
    print("map is %.2f%% faster than list comprehension for count of %i" % (t_list / t_map * 100 - 100, map_count))


main()
