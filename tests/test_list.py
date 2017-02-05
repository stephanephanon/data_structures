from unittest import TestCase
from list import OrderedLinkedList, ListException


class OrderedLinkedListTests(TestCase):
    def test_mixed_classes(self):
        """
        Test that we raise an exception if the element class
        does not define the methods needed for ordering
        """
        class A(object):
            def __init__(self):
                self.x = 7

        l = OrderedLinkedList(A)
        with self.assertRaises(ListException):
            l.add(7)

    def test_first(self):
        l = OrderedLinkedList(int)

        # empty list.
        self.assertEqual(l.size, 0)
        with self.assertRaises(ListException):
            l.first

        # add an item
        l.add(9)
        ret = l.first
        self.assertEqual(l.size, 1)
        self.assertEqual(9, ret)
        self.assertEqual(l.size, 1)

        # add two elements
        l.add(99)
        self.assertEqual(l.size, 2)
        ret = l.first
        self.assertEqual(9, ret)
        self.assertEqual(l.size, 2)

    def test_last(self):
        l = OrderedLinkedList(int)

        # empty list.
        self.assertEqual(l.size, 0)
        with self.assertRaises(ListException):
            l.last

        # add an item
        l.add(9)
        ret = l.last
        self.assertEqual(9, ret)

        # add two elements
        l.add(99)
        ret = l.last
        self.assertEqual(99, ret)

    def test_remove_first(self):
        l = OrderedLinkedList(int)

        # no items - remove
        with self.assertRaises(ListException):
            ret = l.remove_first()

        # 1 item - remove
        l.add(4)
        self.assertEqual(l.size, 1)
        ret = l.remove_first()
        self.assertEqual(ret, 4)
        self.assertEqual(l.size, 0)

        # more than 1 item - remove
        l.add(6)
        l.add(8)
        self.assertEqual(l.size, 2)
        ret = l.remove_first()
        self.assertEqual(ret, 6)
        self.assertEqual(l.size, 1)

    def test_remove_last(self):
        l = OrderedLinkedList(int)

        # no items - remove
        with self.assertRaises(ListException):
            ret = l.remove_last()

        # 1 item - remove
        l.add(4)
        self.assertEqual(l.size, 1)
        ret = l.remove_last()
        self.assertEqual(ret, 4)
        self.assertEqual(l.size, 0)

        # more than 1 item - remove
        l.add(6)
        l.add(8)
        self.assertEqual(l.size, 2)
        ret = l.remove_last()
        self.assertEqual(ret, 8)
        self.assertEqual(l.size, 1)

    def test_contains(self):
        l = OrderedLinkedList(int)

        # empty list
        self.assertFalse(l.contains(4))

        # populated list
        l.add(3)
        l.add(2)
        l.add(5)

        # in the list
        self.assertTrue(l.contains(5))

        # not in the list
        self.assertFalse(l.contains(9))

    def test_is_empty(self):
        l = OrderedLinkedList(int)

        # empty list
        self.assertTrue(l.is_empty)

        # 1 item
        l.add(3)
        self.assertFalse(l.is_empty)

        # multiple items
        l.add(2)
        l.add(4)
        self.assertFalse(l.is_empty)

    def test_size(self):
        l = OrderedLinkedList(int)

        # empty list
        self.assertEqual(l.size, 0)

        # 1 item
        l.add(3)
        self.assertEqual(l.size, 1)

        # multiple items
        l.add(2)
        l.add(4)
        self.assertEqual(l.size, 3)

    def test_add_smaller_than_first(self):
        l = OrderedLinkedList(int)
        l.add(9)
        l.add(1)
        self.assertEqual(l.first, 1)
        self.assertEqual(l.last, 9)

    def test_add_bigger_than_last(self):
        l = OrderedLinkedList(int)
        l.add(3)
        l.add(4)
        self.assertEqual(l.first, 3)
        self.assertEqual(l.last, 4)
        l.add(9)
        self.assertEqual(l.first, 3)
        self.assertEqual(l.last, 9)

    def test_add_mixed_order(self):
        l = OrderedLinkedList(int)
        l.add(2)
        l.add(4)
        l.add(1)
        l.add(3)
        l.add(5)
        expected_ret = [1, 2, 3, 4, 5]
        ret = [i for i in l]
        self.assertEqual(expected_ret, ret)
