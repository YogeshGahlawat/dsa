#!/usr/bin/python3

"""
    GeeksForGeeks Problem #2
    Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.

    Note: There are no duplicates in the list.

    Examples: 
    Input: arr[] = {1, 2, 4, 6, 3, 7, 8} , N = 8
    Output: 5
    Explanation: Here the size of the array is 8, so the range will be [1, 8]. The missing number between 1 to 8 is 5

    Input: arr[] = {1, 2, 3, 5}, N = 5
    Output: 4
    Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4
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

        # Using Brute Force Approach

        data = self.__data
        size = len(self.__data)
        count = 1

        for i in range(size):
            for j in range(size):
                if data[j] == count:
                    count += 1
        return count

    def approach2(self) -> int:
        """
            DESC: Using Mathematial Formula for calcualting the sum of N Natural Numbers
            FORMULA: (N * (N + 1)) / 2
        """

        data = self.__data
        size = len(data)
        sizeN = size + 1

        # Calculate the sum of N Numbers
        sumN = (sizeN * (sizeN + 1)) // 2

        # Calculate the sum of array elements
        sum = 0
        for value in data:
            sum += value

        return sumN - sum

    def approach3(self) -> int:

        # Using Hashing Algorithm
        pass

    def approach4(self) -> int:
        # Using XOR operator
        pass


if __name__ == '__main__':

    data = (1, 2, 3, 5)
    obj = Solution(data)
    # value = obj.approach1()
    # print(f'{value} is the value missing from the array {obj.getData}')

    value = obj.approach2()
    print(f'{value} is the value missing from the array {obj.getData}')
