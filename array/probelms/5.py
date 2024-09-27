#!/usr/bin/python3

"""
Given a binary array arr[] of size N, which is sorted in non-increasing order, count the number of 1’s in it. 

Examples: 

Input: arr[] = {1, 1, 0, 0, 0, 0, 0}
Output: 2

Input: arr[] = {1, 1, 1, 1, 1, 1, 1}
Output: 7

Input: arr[] = {0, 0, 0, 0, 0, 0, 0}
Output: 0
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

    def binarySearch(self, data: tuple, start, end) -> int:

        if start >= end:
            return 0

        mid = start + (end - start) // 2

        count = 0
        if data[mid] == 1:
            count += 1
            count += self.binarySearch(data, start, mid)
            count += self.binarySearch(data, mid + 1, end)
            return count
        elif data[mid] < 1:
            count += self.binarySearch(data, start, mid)
            return count

    def approach1(self) -> int:

        # Using Brute Force Approach
        data = self.__data

        if data is None or len(data) == 0:
            raise ValueError('Dataset ie empty...🥺')

        count = 0
        for value in data:
            if value == 1:
                count += 1

        return count

    def approach2(self) -> int:

        # Using Binary Search, make sure the dataset is in non-increasing order
        data = self.__data

        if data is None or len(data) == 0:
            raise ValueError('Dataset is empty...🥺')

        return self.binarySearch(data, 0, len(data))


if __name__ == '__main__':

    data = (1, 1, 1, 0, 0, 0, 0)
    obj = Solution(data)
    # value = obj.approach1()
    value = obj.approach2()
    if value == 0:
        print('No 1\'s found...🥺')
    else:
        print(f'1\'s found {value} times in {obj.getData}')
