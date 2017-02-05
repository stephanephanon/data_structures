from unittest import TestCase
from linked_lists import DoubleLinkedList, Node


class DoubleLinkedListTests(TestCase):
    """
    Tests on the DoubleLinkedList class
    Mostly to check on next/prev pointer management
    """
    def test_insert_first(self):
        l = DoubleLinkedList()
        l.insert_first(1)
        n = l.first
        m = l.last

        # assertions about the list setup
        self.assertEqual(n, m)
        self.assertIsNone(n.previous_node)
        self.assertIsNone(n.next_node)

        # add a second item
        l.insert_first(2)
        n = l.first
        m = l.last
        self.assertEqual(n.element, 2)
        self.assertEqual(m.element, 1)

        self.assertIsNone(n.previous_node)
        self.assertEqual(n.next_node, m)

        self.assertEqual(m.previous_node, n)
        self.assertIsNone(m.next_node)

        # add a third item
        l.insert_first(3)
        n = l.first
        m = l.first.next_node
        o = l.last

        self.assertEqual(n.element, 3)
        self.assertEqual(m.element, 2)
        self.assertEqual(o.element, 1)

        self.assertIsNone(n.previous_node)
        self.assertEqual(n.next_node, m)

        self.assertEqual(m.previous_node, n)
        self.assertEqual(m.next_node, o)

        self.assertEqual(o.previous_node, m)
        self.assertIsNone(o.next_node)

    def test_insert_last(self):
        l = DoubleLinkedList()
        l.insert_last(1)
        n = l.first
        m = l.last

        # assertions about the list setup
        self.assertEqual(n, m)
        self.assertIsNone(n.previous_node)
        self.assertIsNone(n.next_node)

        # add a second item
        l.insert_last(2)
        n = l.first
        m = l.last
        self.assertEqual(n.element, 1)
        self.assertEqual(m.element, 2)

        self.assertIsNone(n.previous_node)
        self.assertEqual(n.next_node, m)

        self.assertEqual(m.previous_node, n)
        self.assertIsNone(m.next_node)

        # add a third item
        l.insert_last(3)
        n = l.first
        m = l.first.next_node
        o = l.last

        self.assertEqual(n.element, 1)
        self.assertEqual(m.element, 2)
        self.assertEqual(o.element, 3)

        self.assertIsNone(n.previous_node)
        self.assertEqual(n.next_node, m)

        self.assertEqual(m.previous_node, n)
        self.assertEqual(m.next_node, o)

        self.assertEqual(o.previous_node, m)
        self.assertIsNone(o.next_node)

    def test_delete_first_one_element(self):
        l = DoubleLinkedList()
        l.insert_first(1)
        n = l.first
        m = l.last

        # now delete
        ret = l.delete_first()
        self.assertEqual(ret, 1)
        self.assertIsNone(l.first)
        self.assertIsNone(l.last)
        self.assertEqual(n, m)
        self.assertIsNone(n.previous_node)
        self.assertIsNone(n.next_node)

    def test_delete_first_two_element(self):
        l = DoubleLinkedList()
        l.insert_first(1)
        l.insert_first(2)

        # now delete
        ret = l.delete_first()
        self.assertEqual(ret, 2)

        self.assertEqual(l.first.element, 1)
        self.assertEqual(l.last.element, 1)

        self.assertEqual(l.first, l.last)
        self.assertIsNone(l.first.previous_node)
        self.assertIsNone(l.last.next_node)

        # now delete again
        ret = l.delete_first()
        self.assertEqual(ret, 1)

        self.assertIsNone(l.first)
        self.assertIsNone(l.last)

    def test_delete_first_three_element(self):
        l = DoubleLinkedList()
        l.insert_first(1)
        l.insert_first(2)
        l.insert_first(3)

        # now delete
        ret = l.delete_first()
        self.assertEqual(ret, 3)

        self.assertEqual(l.first.element, 2)
        self.assertEqual(l.last.element, 1)

        self.assertIsNone(l.first.previous_node)
        self.assertEqual(l.first.next_node, l.last)
        self.assertEqual(l.last.previous_node, l.first)
        self.assertIsNone(l.last.next_node)

    def test_delete_last_one_element(self):
        l = DoubleLinkedList()
        l.insert_first(1)
        n = l.first
        m = l.last

        # now delete
        ret = l.delete_last()
        self.assertEqual(ret, 1)
        self.assertIsNone(l.first)
        self.assertIsNone(l.last)
        self.assertEqual(n, m)
        self.assertIsNone(n.previous_node)
        self.assertIsNone(n.next_node)

    def test_delete_last_two_element(self):
        l = DoubleLinkedList()
        l.insert_first(1)
        l.insert_first(2)

        # now delete
        ret = l.delete_last()
        self.assertEqual(ret, 1)

        self.assertEqual(l.first.element, 2)
        self.assertEqual(l.last.element, 2)

        self.assertEqual(l.first, l.last)
        self.assertIsNone(l.first.previous_node)
        self.assertIsNone(l.last.next_node)

        # now delete again
        ret = l.delete_last()
        self.assertEqual(ret, 2)

        self.assertIsNone(l.first)
        self.assertIsNone(l.last)

    def test_delete_last_three_element(self):
        l = DoubleLinkedList()
        l.insert_first(1)
        l.insert_first(2)
        l.insert_first(3)

        # now delete
        ret = l.delete_last()
        self.assertEqual(ret, 1)

        self.assertEqual(l.first.element, 3)
        self.assertEqual(l.last.element, 2)

        self.assertIsNone(l.first.previous_node)
        self.assertEqual(l.first.next_node, l.last)
        self.assertEqual(l.last.previous_node, l.first)
        self.assertIsNone(l.last.next_node)
