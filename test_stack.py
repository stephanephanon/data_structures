from unittest2 import TestCase

from stack import ArrayStack

class TestArrayStack(TestCase):
    def test_push(self):
        """
        We can push an item on the stack. We should not get an error
        """
        stack = ArrayStack()

        # nothing sent it
        with self.assertRaises(TypeError):
            stack.push()

        # add a bunch of items and push. no errors
        mixed_list = [1, 'a', [6, 7, 8], {"cat": "sylvester"}, None]
        for item in mixed_list:
            stack.push(item)

    def test_pop(self):
        """
        We can pop an item from the stack
        """
        # empty stack
        stack = ArrayStack()
        with self.assertRaises(IndexError):
            stack.pop()

        # add one thing then pop
        stack.push('a')
        self.assertEqual(stack.pop(), 'a')
        with self.assertRaises(IndexError):
            stack.pop()

        # add 3 things then pop
        stack.push('a')
        stack.push('b')
        stack.push('c')
        self.assertEqual(stack.pop(), 'c')
        self.assertEqual(stack.pop(), 'b')
        self.assertEqual(stack.pop(), 'a')
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek(self):
        # empty stack
        stack = ArrayStack()
        with self.assertRaises(IndexError):
            stack.peek()

        # add one thing then peek. it should still be there
        stack.push('a')
        self.assertEqual(stack.peek(), 'a')
        self.assertEqual(stack.peek(), 'a')

    def test_is_empty(self):
        # empty stack
        stack = ArrayStack()
        self.assertTrue(stack.is_empty())

        # non-empty stack
        stack.push('a')
        self.assertFalse(stack.is_empty())

    def test_size(self):
        # empty stack
        stack = ArrayStack()
        self.assertEqual(stack.size(), 0)

        # one item
        stack.push('a')
        self.assertEqual(stack.size(), 1)

        # +1 item
        stack.push('b')
        self.assertEqual(stack.size(), 2)
