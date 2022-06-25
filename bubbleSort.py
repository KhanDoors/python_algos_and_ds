from pygorithm.sorting import bubble_sort

# print(bubble_sort.get_code())


def sort(_list):
    """
    Bubble Sorting algorithm

    :param _list: list of values to sort
    :return: sorted values
    """
    for i in range(len(_list)):
        for j in range(len(_list) - 1, i, -1):
            if _list[j] < _list[j - 1]:
                _list[j], _list[j - 1] = _list[j - 1], _list[j]
    return _list


mylist = [1, 5, 6, 7, 8, 49, 4, 69, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

print(bubble_sort.sort(mylist))
print(sort(mylist))
