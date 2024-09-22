#!/usr/bin/python3

"""
Program to print the following pattern
    1
    2 1
    3 2 1
    4 3 2 1
"""

if __name__ == '__main__':

    n = int(input("Input No. of lines: "))

    # loop processes the number of lines/rows
    for i in range(1, n+1):
        # loop prints the number starting from i till j > 0 for each row
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
