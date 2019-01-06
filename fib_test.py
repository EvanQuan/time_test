from timer import timer


@timer
def recursive_fib(n):
    """
    This is slower and is limited by the call stack
    """
    return recursive_fib_helper(n)


def recursive_fib_helper(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fib_helper(n-1) + recursive_fib_helper(n-2)


@timer
def dynamic_fib(n):
    return dynamic_fib_helper(n)


def dynamic_fib_helper(n, f={}):
    """

    """
    if n in f:
        return f[n]
    if n == 0 or n == 1:
        f[n] = n
        return f[n]
    else:
        f[n] = dynamic_fib_helper(n-1) + dynamic_fib_helper(n-2)
        #  return dynamic_fib_helper(n-1) + dynamic_fib_helper(n-2)
        return f[n]


@timer
def iterative_fib(n):
    """
    This is much faster than the recursive function

    O(n)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    fm2 = 0
    fm1 = 1
    for i in range(2, n+1):
        current = fm1 + fm2
        fm2 = fm1
        fm1 = current

    return current


value = int(input("Enter an interger: "))

iterative_answer, iterative_time = iterative_fib(value)
dynamic_answer, dynamic_time = dynamic_fib(value)
recursive_answer, recursive_time = recursive_fib(value)

print("Using iteration fib(%d) is" % value, iterative_answer)
print("Using dynamic fib(%d) is" % value, dynamic_answer)
print("Using recursion fib(%d) is" % value, recursive_answer)
