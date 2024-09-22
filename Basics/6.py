#!/usr/bin/python3

# Program to calculate the sum of numbers from 1 to N

if __name__ == '__main__':

    num = int(input('Input a number: '))

    sum = 0

    # Using While loop
    # temp = num
    # while temp > 0:
    #     sum += temp
    #     temp -= 1

    # Using For Loop
    # for i in range(num+1):
    #     sum += i

    # Using Mathematical Formula
    sum = int(num * (num + 1) / 2)

    print(f'Sum of numbers from 1 to {num} is {sum}')
