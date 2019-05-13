from rcviz import viz


# cache = {}
#
# def fib2(n):
#     assert n >= 0
#     if n not in cache:
#         cache[n] = n if n <= 1 else fib(n-1) + fib(n-2)
#
#     return cache[n]


def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


def memo(f):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner


def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


# if __name__ == '__main__':
#     n = 50
#     # fib_func = fib
#     # fib = viz(fib)
#     # fib(10)
#     fib2 = memo(fib1)
#     print(fib2(n))
