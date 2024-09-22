#!/usr/bin/python3

# Program to find the factorial of a given number

if __name__ == '__main__':

    num = int(input("Input a number: "))

    temp = num
    fact = 1
    while temp > 0:
        fact *= temp
        temp -= 1

    print(f'Factorial of {num} is : {fact} ')
