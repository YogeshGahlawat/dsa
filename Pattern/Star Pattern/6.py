#!/usr/bin/python3

"""
Program to print the following pattern
            *
          * * *
        * * * * *
      * * * * * * *
        * * * * *
          * * *
            *
"""


if __name__ == '__main__':

    rows = int(input('Input No. of rows: '))

    # loop will process upper half
    for i in range(rows):
        # loop will print upper left of spaces
        for j in range(rows-1, i, -1):
            print(' ', end=' ')

        # loop will print upper left half of *
        for j in range(i+1):
            print('*', end=' ')

        # loop will print upper right half of *
        for j in range(1, i+1):
            print('*', end=' ')

        print()

    # loop will process lower half
    for i in range(1, rows):
        for j in range(1, i+1):
            print(' ', end=' ')

        for j in range(rows-1, i-1, -1):
            print('*', end=' ')

        for j in range(rows-1, i, -1):
            print('*', end=' ')

        print()
