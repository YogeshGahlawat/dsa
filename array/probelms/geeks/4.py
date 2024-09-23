#!/usr/bin/python3

"""
    GeeksForGeeks
    DESC: Search, Insert, and Delete in an Sorted/Unsorted Array | Array Operations
    Search ==> Linear Search is more efficeient algorithm for searching in an unsorted array...
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

    def linearSearch(self, searchElement: int) -> int:

        data = self.__data

        if data is None or len(data) == 0:
            return -1

        for index, value in enumerate(data):
            if value == searchElement:
                return index
        return -1

    def insertData(self, value: int, position: int) -> None:

        data = list(self.__data)
        size = len(data)

        if position > size:
            raise IndexError(
                'Insetion position can\'t be more than the actual size of the datase...🥺')

        if position == size:
            data.append(value)
        else:
            data.insert(position, value)

        self.__data = tuple(data)

    def deleteData(self, value: int) -> None:

        data = list(self.__data)
        data.remove(value)
        self.__data = tuple(data)


if __name__ == '__main__':

    data = (5, 6, 7, 8, 9, 10)
    searchElement = 10
    obj = Solution(data)
    index = obj.linearSearch(searchElement)
    if index == -1:
        print('Data not found...🥺')
    else:
        print(
            f'Element {searchElement} found at index {index} in dataset {obj.getData} ')

    value = 11
    position = 6
    print(f'Dataset before insert {obj.getData}')
    obj.insertData(value, position)
    print(f'Dataset after insert {obj.getData}')

    value = 11
    print(f'Dataset before removal {obj.getData}')
    obj.deleteData(value)
    print(f'Dataset after removal {obj.getData}')
