"""
Implement a queue api in python
"""
from abc import ABCMeta, abstractmethod


# --------------------------------
# Queue API
# --------------------------------
from linked_lists import LinkedList


class QueueException(Exception):
    """
    QueueABC should raise QueueException for queue errors such as:
    1. no element for first
    2. no element to dequeue
    """
    pass


class QueueABC(metaclass=ABCMeta):  # pragma: no cover
    """
    The queueABC provides the api for a queue data structure (FIFO)

    It also supports the python methods len() and next()
    """
    @abstractmethod
    def enqueue(self, x):
        """
        Add an element to the back of the queue
        :param x: object to add
        :return:
        :raise: TypeError if nothing is queued
        """
        return

    @abstractmethod
    def dequeue(self):
        """
        Remove and return the element at the front of the queue
        :return: element at front
        :raise: QueueException if empty queue
        """
        return

    @abstractmethod
    def first(self):
        """
        Examine and return the element at the front of the queue
        :return: first element
        :raise: QueueException if empty queue
        """
        return

    @abstractmethod
    def is_empty(self):
        """
        Return true if queue is empty else False
        :return: True or False
        """
        return

    @abstractmethod
    def size(self):
        """
        Return the number of elements in the queue
        :return: number of elements
        """
        return


# ----------------------------------------
# Implementation: ArrayQueue
# ----------------------------------------
class CircularArrayQueue(QueueABC):
    """
    Implements queuing with a python list for FIFO operations
    Note: for the purpose of the exercise, we
    pretend that python list does not support arbitrary inserts
    """
    def __init__(self, max_queue_size):
        """
        Initialize a CircularArrayQueue
        :param max_queue_size: max number of items we store in queue
        :return:
        """
        if max_queue_size <= 0:
            raise QueueException("Max_queue_size must be > 0")

        self._max_queue_size = max_queue_size
        self._array = [None]*max_queue_size
        # index of first element
        self._front_index = 0
        # index of next rear element
        self._rear_index = 0
        # number of items in the queue
        self._count = 0

    def first(self):
        """
        Examine and return the element at the front of the queue
        :return: first element
        :raise: QueueException if empty queue
        """
        # if there is nothing in the queue then raise an exception
        if self.is_empty():
            raise QueueException("Cannot fetch first from empty queue")

        # fetch our item
        return self._array[self._front_index]

    def enqueue(self, x):
        """
        Add an element to the back of the queue.
        Note: this method will wrap around and delete the
        items in the front of the line if the queue is full.
        :param x: object to add
        :return:
        :raise: TypeError if nothing is queued
        """
        self._array[self._rear_index] = x
        self._rear_index = (self._rear_index + 1) % self._max_queue_size
        if self._count < self._max_queue_size:
            self._count += 1

    def __len__(self):
        """
        Return the length of the queue
        :return: number of elements
        """
        return self._count

    def size(self):
        """
        Return the number of elements in the queue
        :return: number of elements
        """
        return self._count

    def dequeue(self):
        """
        Remove and return the first element in the queue
        :return: first element
        """
        # if there is nothing in the queue then raise an exception
        if self.is_empty():
            raise QueueException("Cannot dequeue from empty queue")

        # fetch our item
        ret = self._array[self._front_index]
        self._array[self._front_index] = None
        self._front_index = (self._front_index + 1) % self._max_queue_size
        if self._count > 0:
            self._count -= 1
        return ret

    def is_empty(self):
        """
        Return true if queue is empty else False
        :return: True or False
        """
        return True if self._count == 0 else False

    def is_full(self):
        """
        Return true if the queue is full.
        :return: True or False
        """
        return True if self._count == self.max_queue_size else False

    @property
    def max_queue_size(self):
        return self._max_queue_size


# ----------------------------------------
# Implementation: Python List Queue
# ----------------------------------------
class PythonListQueue(QueueABC):
    """
    Implementation of the queue data structure
    using a python list for FIFO operations
    """
    def __init__(self):
        self._list = []

    def enqueue(self, x):
        """
        Add an element to the back of the queue
        :param x: object to add
        :return:
        :raise: TypeError if nothing is queued
        """
        self._list.append(x)

    def dequeue(self):
        """
        Remove and return the element at the front of the queue
        :return: element at front
        :raise: QueueException if empty queue
        """
        try:
            return self._list.pop(0)
        except IndexError:
            raise QueueException("Cannot dequeue from empty queue")

    def first(self):
        """
        Examine and return the element at the front of the queue
        :return:
        :raise: QueueException if empty queue
        """
        try:
            return self._list[0]
        except IndexError:
            raise QueueException("Cannot fetch first from empty queue")

    def is_empty(self):
        """
        Return true if queue is empty else False
        :return: True or False
        """
        return True if len(self._list) == 0 else False

    def __len__(self):
        """
        Return the length of the queue
        :return: number of elements
        """
        return len(self._list)

    def size(self):
        """
        Return the number of elements in the queue
        :return: number of elements
        """
        return len(self._list)


# ----------------------------------------
# Implementation: LinkedListQueue
# ----------------------------------------
class LinkedListQueue(QueueABC):
    """
    Implementation of the queue data structure
    using a linked list for FIFO operations
    """
    def __init__(self):
        self._list = LinkedList()

    def first(self):
        """
        Examine and return the element at the front of the queue
        :return: first element
        :raise: QueueException if empty queue
        """
        # if there is nothing in the queue then raise an exception
        if self.is_empty():
            raise QueueException("Cannot fetch first from empty queue")
        return self._list.first.element

    def enqueue(self, x):
        """
        Add an element to the back of the queue.
        :param x: object to add
        :return:
        :raise: TypeError if nothing is queued
        """
        self._list.insert_last(x)

    def __len__(self):
        """
        Return the length of the queue
        :return: number of elements
        """
        return len(self._list)

    def size(self):
        """
        Return the number of elements in the queue
        :return: number of elements
        """
        return len(self._list)

    def dequeue(self):
        """
        Remove and return the first element in the queue
        :return: first element
        """
        # if there is nothing in the queue then raise an exception
        if self.is_empty():
            raise QueueException("Cannot dequeue from empty queue")

        return self._list.delete_first()

    def is_empty(self):
        """
        Return true if queue is empty else False
        :return: True or False
        """
        return True if len(self._list) == 0 else False

