#!/usr/bin/python3

"""
Program to print the following pattern
    *
    * *
    * * *
    * * * *
"""


if __name__ == '__main__':
    n = int(input("Enter No. of lines: "))

    # loop process the no of rows
    for i in range(n):
        # loop prints * for each row
        for j in range(i+1):
            print("*", end=' ')
        print()
