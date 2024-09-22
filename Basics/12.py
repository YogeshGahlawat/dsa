#!/usr/bin/python3

"""
Program to calculate the binomial co-efficient for nCr
    nCr = n! / r! (n-r)!
"""


def fact(n):
    fact = 1
    while (n > 0):
        fact *= n
        n -= 1
    return fact


def binomialCoefficient(n, r):
    nfact = fact(n)
    rfact = fact(r)
    nrfact = fact(n - r)

    return nfact // (rfact * nrfact)


if __name__ == '__main__':

    n = int(input("Input value for n: "))
    r = int(input("Input value for r: "))

    print(binomialCoefficient(n, r))
