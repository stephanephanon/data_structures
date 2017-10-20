"""
implementations of several different sorting algorithms in python
"""


def bubble_sort(data):
    """
    Sort the data by 'bubbling up' and
    comparing adjacent pairs of values.
    Each time we will loop for one less at the end
    (because we already sorted those items). O(n^2)
    :param data: list to sort
    :return: None. modifies data param
    """
    for j in range(len(data), 0, -1):
        for i in range(0, j - 1):
            # it's bigger, so swap!
            if data[i] > data[i + 1]:
                data[i + 1], data[i] = data[i], data[i + 1]
    return


def selection_sort(data):
    """
    Sort the data by selecting the smallest element
    and swapping it in place. O(n^2)
    :param data: list to sort
    :return: None. modifies data param
    """
    for j in range(0, len(data)):
        smallest = data[j]
        smallest_index = j
        for i in range(j, len(data)):
            element = data[i]
            if smallest > element:
                smallest = element
                smallest_index = i
        first_element = data[j]
        data[j] = smallest
        data[smallest_index] = first_element
    return


def insertion_sort(data):
    """
    Sort the data by taking an element and inserting
    it where it belongs in the list via a series of swaps.
    O(n^2)... but works better than the previous two
    :param data: list to sort
    :return: None. modifies data param
    """
    for j in range(1, len(data)):
        for i in range(j, 0, -1):
            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]

    return


def shell_sort(data):
    """
    An improved insertion sort. Break the list
    into sublists, and sort those by insertion_sort.
    Will be between O(n) and O(n^2)
    :param data: list to sort
    :return: None. modifies data param
    """
    gap = len(data) // 2
    while gap > 0:
        for i in range(gap, len(data)):
            element = data[i]
            j = i
            while j >= gap and data[j - gap] > element:
                data[j] = data[j - gap]
                j -= gap
            data[j] = element
        gap //= 2
    return


def merge_sort(data):
    """
    Sort the list by recursively splitting the list, then merging
    the sorted lists back together until done. O(n log n)
    :param data: list to sort
    :return: None. modifies data param
    """
    # base case. 0 or 1 elements is sorted
    if len(data) <= 1:
        return

    # items to sort; recurse to split
    middle_index = len(data)//2
    left = data[:middle_index]
    right = data[middle_index:]
    merge_sort(left)
    merge_sort(right)

    # merge
    # for each half, order and switch in place
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    # only the list with more items will be entered here
    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1

    return

def quick_sort(data):
    pass
