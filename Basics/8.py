#!/usr/bin/python3

# Program to Calculate simple interest

if __name__ == '__main__':

    p = int(input("Input Principle Amount: "))

    r = int(input("Input rate of interest: "))

    t = int(input("Input time period: "))

    si = (p * r * t) / 100

    print(f"Simple Interest: {si}")
