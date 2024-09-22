#!/usr/bin/python3

"""
Program to print the following pattern
        *
      * * *
    * * * * *
  * * * * * * *

"""


if __name__ == '__main__':

    rows = int(input('Input No. of rows: '))

    # loop will process each rows
    for i in range(rows):
        # loop will print spaces
        for j in range(rows-1, i, -1):
            print(' ', end=' ')

        # loop will print left half of *
        for j in range(i+1):
            print('*', end=' ')

        # loop will print right half of *
        for j in range(1, i+1):
            print('*', end=' ')
        print()
