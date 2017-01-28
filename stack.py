"""
Implement a stack api in python
"""
from abc import ABCMeta, abstractmethod

# --------------------------------
# Stack API
# --------------------------------
from linked_lists import LinkedList


class StackException(Exception):
    """
    StackABC should raise StackException for stack errors such as:
    1. no element to peek
    2. no element to pop
    """
    pass


class StackABC(metaclass=ABCMeta):  # pragma: no cover
    """
    The stack abc provides the api for a stack data structure

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
        return

    @abstractmethod
    def pop(self):
        """
        Pop an object from the stack
        :return: popped object
        :raise: StackException if nothing to pop
        """
        return

    @abstractmethod
    def peek(self):
        """
        Peek at the top element of the stack
        :return: data about top element
        :raise: StackException if nothing to peek
        """
        return

    @abstractmethod
    def is_empty(self):
        """
        Return true if empty else false
        :return:
        """
        return

    @abstractmethod
    def size(self):
        """
        Return the size of the stack
        :return:
        """
        return

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
        self.array = []

    def __len__(self):
        return self.size()

    def __iter__(self):
        for i in self.array:
            yield i

    def size(self):
        return len(self.array)

    def peek(self):
        try:
            return self.array[self.size()-1]
        except IndexError:
            raise StackException("Cannot peek into empty stack")

    def push(self, x):
        self.array.append(x)

    def is_empty(self):
        return False if self.array else True

    def pop(self):
        try:
            return self.array.pop()
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
        self.list = LinkedList()

    def __len__(self):
        return self.size()

    def __iter__(self):
        for i in self.list:
            yield i

    def size(self):
        return len(self.list)

    def peek(self):
        """
        Return the obj, but leave it on the stack
        :return:
        """
        if self.list.first:
            return self.list.first.element
        else:
            raise StackException("Cannot peek into empty stack")

    def push(self, x):
        """
        Always push from front of list
        :param x: object to push on stack
        :return:
        """
        self.list.insert_first(x)

    def is_empty(self):
        return False if len(self.list) else True

    def pop(self):
        """
        Pop newest object and return it
        :return: newest object or None
        """
        if len(self.list):
            return self.list.delete_first()
        else:
            raise StackException("Cannot pop from empty stack")

