#!/usr/bin/python3

# Program to check whether a number if prime or not

if __name__ == '__main__':

    num = int(input('Input a number: '))
    isPrime = True

    if (num > 3):
        count = 2
        temp = num - 1
        while (count <= num / 2):
            if (num % count == 0 or num % temp == 0):
                isPrime = False
                break
            count += 1
            temp -= 1

    if (isPrime):
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')
