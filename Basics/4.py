#!/usr/bin/python3

# Program to find the minimum out of 2 numbers

if __name__ == '__main__':

    num1 = int(input('Input 1st number: '))
    num2 = int(input('Input 1st number: '))

    if num1 < num2:
        print(f'{num1} is the smallest number out of {num1} & {num2}')
    else:
        print(f'{num2} is the smallest number out of {num1} & {num2}')
