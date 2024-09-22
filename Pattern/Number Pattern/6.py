#!/usr/bin/python3

"""
Prpgram to print Floyd's triangle
    1
    2 3
    4 5 6
    7 8 9 10
"""


if __name__ == '__main__':

    n = int(input("Input No. of lines: "))

    # count variable is used to process number for each iteration
    count = 1

    # loop processes the number of lines/rows
    for i in range(1, n+1):
        # loop prints the value of count and increments it by 1
        for j in range(1, i + 1):
            print(count, end=" ")
            count += 1
        print()
