"""
Implement a stack api in python
"""
from abc import ABCMeta, abstractmethod


from linked_lists import LinkedList


# --------------------------------
# Stack API
# --------------------------------
class StackException(Exception):
    """
    StackABC should raise StackException for stack errors such as:
    1. no element to peek
    2. no element to pop
    """
    pass


class StackABC(metaclass=ABCMeta):  # pragma: no cover
    """
    The stack abc provides the api for a stack data structure (LIFO)

    It also supports the python methods len() and next()
    """
    @abstractmethod
    def push(self, x):
        """
        Push x onto the stack
        :param x: object
        :return:
        :raise: TypeError if nothing is pushed
        """
        pass

    @abstractmethod
    def pop(self):
        """
        Pop an object from the stack
        :return: popped object
        :raise: StackException if nothing to pop
        """
        pass

    @abstractmethod
    def peek(self):
        """
        Peek at the top element of the stack
        :return: data about top element
        :raise: StackException if nothing to peek
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Return true if empty else false
        :return:
        """
        pass

    @abstractmethod
    def size(self):
        """
        Return the size of the stack
        :return:
        """
        pass

    @abstractmethod
    def __iter__(self):
        """
        Provide support for iteration.
        Should either return a generator,
        or define __iter__ and __next__
        """
        pass

    @abstractmethod
    def __len__(self):
        """
        Provide support for python's len method
        """
        pass


# ----------------------------------------
# Implementation: ArrayStack
# ----------------------------------------
class ArrayStack(StackABC):
    """
    Implementation of the stack data structure
    using an array for LIFO operations
    """
    def __init__(self):
        self._array = []

    def __len__(self):
        return self.size()

    def __iter__(self):
        for i in self._array:
            yield i

    def size(self):
        """
        Return the number of elements in the stack
        """
        return len(self._array)

    def peek(self):
        """
        Return the top element on the stack
        """
        try:
            return self._array[self.size()-1]
        except IndexError:
            raise StackException("Cannot peek into empty stack")

    def push(self, x):
        """
        Add a new element x to the top of the stack
        """
        self._array.append(x)

    def is_empty(self):
        """
        Return True if empty stack else False
        """
        return False if self._array else True

    def pop(self):
        """
        Remove the first element from the stack and return it
        """
        try:
            return self._array.pop()
        except IndexError:
            raise StackException("Cannot pop from empty stack")


# ----------------------------------------
# Implementation: LinkedListStack
# ----------------------------------------
class LinkedListStack(StackABC):
    """
    Implementation of the stack data structure
    using a linked list for LIFO operations
    """
    def __init__(self):
        self._list = LinkedList()

    def __len__(self):
        return self.size()

    def __iter__(self):
        for i in self._list:
            yield i

    def size(self):
        """
        Return number of items in stack
        """
        return len(self._list)

    def peek(self):
        """
        Return the obj, but leave it on the stack
        :return: object
        :raise: StackException
        """
        if self._list.first:
            return self._list.first.element
        else:
            raise StackException("Cannot peek into empty stack")

    def push(self, x):
        """
        Add element x to top of stack
        :param x: object to push on stack
        :return:
        """
        self._list.insert_first(x)

    def is_empty(self):
        """
        Return True if empty stack else False
        :return: True/False
        """
        return False if len(self._list) else True

    def pop(self):
        """
        Remove element from top of stack and return it
        :return: newest object
        :raise: StackException
        """
        if len(self._list):
            return self._list.delete_first()
        else:
            raise StackException("Cannot pop from empty stack")

