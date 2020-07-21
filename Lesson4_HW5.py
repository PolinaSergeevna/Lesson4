from functools import reduce

a = range(100, 1002, 2)


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, a))
