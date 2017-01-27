"""
Implement a stack api in python
"""
from abc import ABCMeta, abstractmethod

# --------------------------------
# Stack API
# --------------------------------
class StackABC(metaclass=ABCMeta):
    """
    The stack abc provides the api for a stack datastructure
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
        :raise: Exception if nothing to pop
        """
        return

    @abstractmethod
    def peek(self):
        """
        Peek at the top element of the stack
        :return: data about top element
        :raise: exception if nothing to peek
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


# ----------------------------------------
# Implementation: ArrayStack
# ----------------------------------------
class ArrayStack(StackABC):
    """
    Implementation of the stack data structure
    that supports LIFO operations
    """
    def __init__(self):
        self.array = []

    def size(self):
        return len(self.array)

    def peek(self):
        return self.array[self.size()-1]

    def push(self, x):
        self.array.append(x)

    def is_empty(self):
        return False if self.array else True

    def pop(self):
        return self.array.pop()
