#!/usr/bin/python3

"""
Program to print the following pattern
    1
    2 2
    3 3 3
    4 4 4 4
"""

if __name__ == '__main__':
    n = int(input("Input No. of lines: "))

    # loop processes the number of lines/rows
    for i in range(1, n+1):
        # loop prints the number same as i
        for j in range(1, i+1):
            print(i, end=' ')
        print()
