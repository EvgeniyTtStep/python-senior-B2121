"""
>>> 2+2
5
"""


def add(*args, **kwargs):
    res = 0
    for i in args:
        res += i

    for value in kwargs.values():
        res += value
    return res




if __name__ == "__main__":
    import doctest

    doctest.testmod()
