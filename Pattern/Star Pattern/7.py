#!/usr/bin/python3

"""
Program to print the following pattern
    *         *
    * *     * *
    * * * * * *
    * *     * *
    *         *
"""


if __name__ == '__main__':

    n = int(input("Input No. of lines: "))

    # Upper half
    # loop processes the no of rows
    for i in range(n):

        # Upper left half
        # loop prints the upper's left half with astrick *
        for j in range(i+1):
            print("*", end=' ')

        # loop prints the upper's left half with spaces
        for j in range(n - i - 1, 0, -1):
            print(' ', end=' ')

        # Upper Right half
        # loop prints the upper's right half with astrick *
        for j in range(n - i - 1, 0, -1):
            print(' ', end=' ')

        # loop prints the upper's right half with astrick *
        for j in range(i+1):
            print("*", end=' ')
        print()

    # Lower Half
    # loop processes the no of rows
    for i in range(n-1):

        # Upper left half
        # loop prints the upper's left half with spaces
        for j in range(n - i - 1, 0, -1):
            print("*", end=' ')

        # loop prints the upper's left half with astrick *
        for j in range(i+1):
            print(' ', end=' ')

        # Upper Right half
        # loop prints the upper's right half with astrick *
        for j in range(i+1):
            print(' ', end=' ')

        # loop prints the upper's right half with astrick *
        for j in range(n - i - 1, 0, -1):
            print("*", end=' ')

        print()
