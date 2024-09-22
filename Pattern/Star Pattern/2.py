#!/usr/bin/python3

"""
Program to print the following pattern
    * * * * *
    *       *
    *       *
    * * * * *
"""

if __name__ == '__main__':

    n = int(input('Input the No. of rows: '))

    # loop processes the no of rows
    for i in range(n):
        # loop prints * for each row based on some conditional
        for j in range(n):
            if (i == 0 or i == n-1 or j == 0 or j == n-1):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
