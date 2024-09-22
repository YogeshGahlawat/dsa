#!/usr/bin/python3

"""
Program to print the following pattern
      *
    * *
  * * *
* * * *
"""

if __name__ == '__main__':

    n = int(input('Input No. of rows: '))

    # loop will process each rows
    for i in range(n):
        # loop will print spaces
        for j in range(n-1, i, -1):
            print(' ', end=' ')

        # loop will print * for each row
        for j in range(i+1):
            print('*', end=' ')
        print()
