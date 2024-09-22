#!/usr/bin/python3

"""
Program to print the following pattern
    1
    1 2
    1 2 3
    1 2 3 4
"""

if __name__ == '__main__':
    n = int(input("Input No. of lines: "))

    # loop processes the no of lines/rows
    for i in range(1, n + 1):
        # loop prints the number starting from 1 till j <= i for each row
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
