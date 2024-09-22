#!/usr/bin/python3

"""
    DESC: Implementation of searching algorithms using OOPs
    ALGO:
            1) Linear Search ==> Linear Search uses Brute-Force Approach to search for a element in the search space...
            2) Binary Search ==> Binary Search uses Divide and Conquor Approach to search for a element in the search spcace...
                For Binary Search, dataset must be in sorted order before searching for a record...
"""


class SearchRecord:

    def __init__(self, data: tuple) -> None:
        print('Initializing the data for searchRecord Class...😌')
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

    def linearSearch(self, searchElement: int) -> int:

        data = self.__data

        if data is None or len(data) == 0:
            return -1

        for index, value in enumerate(data):
            if value == searchElement:
                return index

        return -1

    def linearRecursion(self, searchElement: int, searchIndex=0) -> int:

        data = self.__data
        if searchIndex == len(data) or data is None:
            return -1

        if data[searchIndex] == searchElement:
            return searchIndex

        return self.linearRecursion(searchElement, searchIndex+1)

    def binarySearch(self, searchElement: int, isAsc=True) -> int:

        data = self.__data

        if data is None or len(data) == 0:
            return -1

        low = 0
        high = len(data)

        while low < high:

            mid = low + (high - low) // 2

            if data[mid] == searchElement:
                return mid
            if isAsc:
                if data[mid] < searchElement:
                    low = mid + 1
                else:
                    high = mid
            else:
                if data[mid] > searchElement:
                    low = mid + 1
                else:
                    high = mid
        else:
            return -1

    def binaryRecursion(self, searchElement: int, startIndex: int, lastIndex: int, isAsc=True) -> int:

        data = self.__data

        if startIndex == lastIndex or data is None:
            return -1

        mid = startIndex + (lastIndex-startIndex) // 2

        if data[mid] == searchElement:
            return mid
        if isAsc:
            if data[mid] < searchElement:
                return self.binaryRecursion(searchElement, mid+1, lastIndex)
            else:
                return self.binaryRecursion(searchElement, startIndex, mid)
        else:
            if data[mid] > searchElement:
                return self.binaryRecursion(searchElement, mid+1, lastIndex)
            else:
                return self.binaryRecursion(searchElement, startIndex, mid)


if __name__ == '__main__':

    data = (1, 2, 3, 4, 5)
    searchElement = 1

    # # While the data is availble in ascending order
    # obj = SearchRecord(data)
    # index = obj.linearSearch(searchElement)
    # index = obj.linearRecursion(searchElement)
    # index = obj.binarySearch(searchElement)

    # # While the data is availble in descending order
    obj = SearchRecord(sorted(data, reverse=True))
    # index = obj.binarySearch(searchElement, isAsc=False)
    index = obj.binaryRecursion(searchElement, 0, len(data), isAsc=False)
    print(obj)
    if index == -1:
        print('Either the data set is empty or element not found...🥺')
    else:
        print(f'Element {searchElement} found at {index} in {obj.getData}')
