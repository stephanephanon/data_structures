from unittest import TestCase
from sorts.sorting_algorithms import bubble_sort, selection_sort, insertion_sort, shell_sort, merge_sort


class BubbleSortTests(TestCase):
    """
    Tests on the bubble sort function
    """
    def test_empty_list(self):
        l = []
        bubble_sort(l)
        self.assertEqual(len(l), 0)

    def test_single_item_list(self):
        l = [9]
        bubble_sort(l)
        self.assertEqual(len(l), 1)

    def test_already_sorted_list(self):
        l = [1, 3, 9, 13]
        bubble_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])

    def test_reverse_sorted_list(self):
        l = [13, 9, 3, 1]
        bubble_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])

    def test_unsorted_list(self):
        l = [9, 1, 3, 13]
        bubble_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])


class SelectionSortTests(TestCase):
    """
    Tests on the selection sort function
    """
    def test_empty_list(self):
        l = []
        selection_sort(l)
        self.assertEqual(len(l), 0)

    def test_single_item_list(self):
        l = [9]
        selection_sort(l)
        self.assertEqual(len(l), 1)

    def test_already_sorted_list(self):
        l = [1, 3, 9, 13]
        selection_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])

    def test_reverse_sorted_list(self):
        l = [13, 9, 3, 1]
        selection_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])

    def test_unsorted_list(self):
        l = [9, 1, 3, 13]
        selection_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])


class InsertionSortTests(TestCase):
    """
    Tests on insertion sort function
    """
    def test_empty_list(self):
        l = []
        insertion_sort(l)
        self.assertEqual(len(l), 0)

    def test_single_item_list(self):
        l = [9]
        insertion_sort(l)
        self.assertEqual(len(l), 1)

    def test_already_sorted_list(self):
        l = [1, 3, 9, 13]
        insertion_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])

    def test_reverse_sorted_list(self):
        l = [13, 9, 3, 1]
        insertion_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])

    def test_unsorted_list(self):
        l = [9, 1, 3, 13]
        insertion_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])


class ShellSortTests(TestCase):
    """
    Tests on the shell sort function
    """
    def test_empty_list(self):
        l = []
        shell_sort(l)
        self.assertEqual(len(l), 0)

    def test_single_item_list(self):
        l = [9]
        shell_sort(l)
        self.assertEqual(len(l), 1)

    def test_already_sorted_list(self):
        l = [1, 3, 9, 13]
        shell_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])

    def test_reverse_sorted_list(self):
        l = [13, 9, 3, 1]
        shell_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])

    def test_unsorted_list(self):
        l = [9, 1, 3, 13]
        shell_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])


class MergeSortTests(TestCase):
    """
    Tests on the merge sort function
    """
    def test_empty_list(self):
        l = []
        merge_sort(l)
        self.assertEqual(len(l), 0)

    def test_single_item_list(self):
        l = [9]
        merge_sort(l)
        self.assertEqual(len(l), 1)

    def test_already_sorted_list(self):
        l = [1, 3, 9, 13]
        merge_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])

    def test_reverse_sorted_list(self):
        l = [13, 9, 3, 1]
        merge_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])

    def test_unsorted_list(self):
        l = [9, 1, 3, 13]
        merge_sort(l)
        self.assertEqual(l, [1, 3, 9, 13])