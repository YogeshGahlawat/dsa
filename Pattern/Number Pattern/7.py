#!/usr/bin/python3

"""
Program to print the following pattern
    1 1 1 1
      2 2 2
        3 3
          4
"""

if __name__ == '__main__':
    n = int(input("Input No. of lines: "))

    # loop processes the no of lines/rows
    for i in range(1, n+1):
        # loop prints the spaces starting from 1 till j < i
        for j in range(1, i):
            print(" ", end=" ")

        # loop prints the values of i starting from max value(n) till j >= i
        for j in range(n, i-1, -1):
            print(i, end=" ")
        print()
