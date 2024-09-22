#!/usr/bin/python3

"""
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
"""


if __name__ == '__main__':

    n = int(input("Input No. of lines: "))

    # count variable is used to process number for each iteration
    count = 1
    # loop processes the no of lines/rows
    for i in range(n):
        # loop prints the value of count and increments it by 1
        for j in range(n):
            print(count, end=" ")
            count += 1
        print()
