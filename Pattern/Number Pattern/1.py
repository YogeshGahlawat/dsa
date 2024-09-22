#!/usr/bin/python3

"""
Prpgram to print the following pattern
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5

DESC: 1) Outer Loop processes the no of lines/rows
      2) Inner loop prints the numbers starting from 1 to n for each rows
"""


if __name__ == '__main__':

    n = int(input("Enter No. of line: "))

    # loop processes the no of rows/lines
    for i in range(1, n + 1):
        # loop will print numbers starting from 1 to n for each row
        for j in range(1, n + 1):
            print(j, end=' ')
        print()
