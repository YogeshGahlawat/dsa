#!/usr/bin/python3

"""
Given an array of integers arr[], The task is to find the index of first repeating element in it i.e. the element that occurs more than once and whose index of the first occurrence is the smallest. 

Examples: 

Input: arr[] = {10, 5, 3, 4, 3, 5, 6}
Output: 5 
Explanation: 5 is the first element that repeats

Input: arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
Output: 6 
Explanation: 6 is the first element that repeats
"""


class Solution:

    def __init__(self, data: tuple) -> None:
        print(
            f'Initializing the data for {str(self.__class__).split(".")[-1][:-2]} Class...😌')
        self.__data = data

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

    def approach1(self) -> int:

        # Brute Force Approach

        data = self.__data

        if data is None or len(data) == 0:
            raise ValueError('Dataset is empty...🥺')

        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[j] == data[i]:
                    return data[i]
        else:
            return -1


if __name__ == '__main__':

    data = (10, 5, 3, 4, 3, 6)
    obj = Solution(data)
    value = obj.approach1()
    if value == -1:
        print('No element repetition found...🥺')
    else:
        print(f'{value} is the first element that repeats in dataset {obj.getData}')
