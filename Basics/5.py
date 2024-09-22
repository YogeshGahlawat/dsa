#!/usr/bin/python3

# Program to find whether a number is even or odd

if __name__ == '__main__':

    num = int(input('Input a number: '))

    if num == 0:
        print(f'{num} neither a even nor a odd number')
    else:
        if num % 2:
            print(f'{num} is the odd number')
        else:
            print(f'{num} is the even number')
