#!/usr/bin/python3

"""
Program to print pyramid pattern
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1

DESC: 1) Outer Loop processes the no of lines/rows
      2) First inner loop prints spcaes for pyramid's left half.
         For each row, loop prints spaces starting from the max size(n) - 1 till the value of j >= i.
      3) Second inner loop prints numbers for pyramid's left half.
         For each row, loop prints numbers starting  starting from 1 till the value of j <= i.
      4) Third Inner Loop prints numbers for pyramid's right half.
         For each row, loop prints numbers starting from current line(i) - 1 till j > 0.
"""

if __name__ == '__main__':

    n = int(input("Input No. of lines: "))

    # loop will process no of rows/lines
    for i in range(1, n + 1):
        # For each row, loop prints spaces starting from the max size(n) - 1 till the value of j >= i.
        for j in range(n-1, i-1, -1):
            print(" ", end=" ")

        # For each row, loop prints numbers starting  starting from 1 till the value of j <= i.
        for j in range(1, i + 1):
            print(j, end=" ")

        # For each row, loop prints numbers starting from current line(i) - 1 till j > 0.
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()
