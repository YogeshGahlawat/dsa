#!/usr/bin/python3

# Program to find maximum out of 2 given numbers

if __name__ == '__main__':

    num1 = int(input("Input 1st number: "))
    num2 = int(input("Input 2nd number: "))

    if num1 > num2:
        print(f'{num1} is largest number out of {num1} & {num2}')
    else:
        print(f'{num2} is largest number out of {num1} & {num2}')
