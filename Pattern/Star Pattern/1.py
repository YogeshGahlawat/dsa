#!/usr/bin/python3

"""
Program to print following Pattern
    * * * * *
    * * * * *
    * * * * *
    * * * * *
"""

if __name__ == '__main__':

    n = int(input("Enter No. of line: "))

    # loop processes the no of rows
    for i in range(n):
        # loop prints no of * for each line
        for j in range(n):
            print("*", end=' ')
        print()
