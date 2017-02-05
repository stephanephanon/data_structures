from abc import ABCMeta, abstractmethod


# --------------------------------
# List APIs
# --------------------------------
class ListABC(metaclass=ABCMeta):
    """
    The ListABC provides the api for a basic list data structure
    """
    @abstractmethod
    def first(self):
        """
        Examine the element at the front of the list
        :return: element at front
        """
        pass

    @abstractmethod
    def last(self):
        """
        Examine the element at the rear of the list
        :return: element at rear
        """
        pass

    @abstractmethod
    def remove_firt(self):
        """
        Remove and return the element at the front of the list
        :return: element at front
        """
        pass

    @abstractmethod
    def remove_last(self):
        """
        Remove and return the element at the rear of the list
        :return: element at rear
        """
        pass

    @abstractmethod
    def contains(self, x):
        """
        Return True if list contains element x, else False
        :param x: object to check for
        :return: True if in list, else False
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Return True if list is empty, else False
        :return: True if empty, else False
        """
        pass

    @abstractmethod
    def size(self):
        """
        Return the size (number of elements) in the list
        :return: size of list
        """
        pass


class OrderedListABC(ListABC, metaclass=ABCMeta):
    """
    The OrderedListABC provides the api for an ordered list
    """
    @abstractmethod
    def add(self, x):
        """
        Add element x to the list at its appropriate spot
        param x: element to add
        """
        pass


class UnorderedListABC(ListABC, metaclass=ABCMeta):
    @abstractmethod
    def add_to_front(self, x):
        """
        Add element x to the front of the list
        :param x: element to add
        """
        pass

    @abstractmethod
    def add_to_rear(self, x):
        """
        Add element x to the rear of the list
        :param x: element to add
        """
        pass

    @abstractmethod
    def add_after(self, obj, new_obj):
        """
        Add element new_obj after obj.
        :param obj: existing element in the list
        :param new_obj: new element to add
        :return:
        """
        pass


# --------------------------------
# Ordered List Implementation
# --------------------------------