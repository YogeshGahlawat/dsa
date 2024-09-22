#!/usr/bin/python3

# Program to check whether a person should get driving licence or not based on given age

if __name__ == '__main__':

    age = int(input("Input age in years: "))

    if age > 18:
        print("Driving Licence should be approved")
    else:
        print("Driving Licence should not be approved")
