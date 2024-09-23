#!/usr/bin/python3


"""
    GeekForGeeks Problem #1
    DESC: Given an array with all distinct elements, find the largest three elements.

    Examples :
    Input: arr[] = {10, 4, 3, 50, 23, 90}
    Output: 90, 50, 23

    Input: arr[] = { 6, 8, 9, 2, 1, 10}
    Output: 10, 8, 9
    
    HINT:   1) Brute Force Approach
"""

import sys


class Solution:

    def __init__(self, data: tuple) -> None:
        print(
            f'Initializing the data for {str(self.__class__).split(".")[-1][:-2]} Class...😌')
        self.__data = data
        self.__first = -sys.maxsize - 1
        self.__second = -sys.maxsize - 1
        self.__third = -sys.maxsize - 1

    def __repr__(self) -> str:
        return f'{str(self.__class__).split(".")[-1][:-2]}({self.__data})'

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def getData(self) -> str:

        data = self.__data

        if data is None or len(data) == 0:
            return None

        result = ' { '

        for index, value in enumerate(data):
            if index == len(data) - 1:
                result += str(value)
            else:
                result += f'{value}, '
        result += ' }'
        return result

    def bruteForceApproach(self) -> tuple:

        data = self.__data

        if data is None or len(data) == 0:
            raise ValueError('Data Set is empty...🥺')

        if len(data) < 3:
            raise ValueError('Insufficient Values...🥺')

        for value in data:

            if value > self.__third:
                self.__third = value

            if self.__third > self.__second:
                self.__second, self.__third = self.__third, self.__second

            if self.__second > self.__first:
                self.__first, self.__second = self.__second, self.__first

        return self.__first, self.__second, self.__third


if __name__ == '__main__':

    data = (10, 4, 3, 50, 23, 90)

    obj = Solution(data)
    first, second, third = obj.bruteForceApproach()
    print(f'{first} is the 1st largest element in {obj.getData}')
    print(f'{second} is 2nd largest element in {obj.getData}')
    print(f'{third} is the 3rd largest element in {obj.getData}')
