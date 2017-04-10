from __future__ import print_function
import sys

def fact(n):
    """
    Factorial function

    :arg n: Number
    :returns: factorial of n
    """

    if n == 0:
        return 1
    resp = n * fact(n - 1)
    print(resp)
    return resp

def div(n, m):
    """
    Just divide
    """
    res = n / m
    return res


def main(n):
    res = fact(n)
    print(res)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))