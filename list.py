from abc import ABCMeta, abstractmethod, abstractproperty


# --------------------------------
# List APIs
# --------------------------------
from linked_lists import LinkedList, Node


class ListException(Exception):
    """
    ListABC should raise ListException for list errors such as:
    1. no element for first
    2. wrong class type for ordered list
    3. no element to remove
    """

class ListABC(metaclass=ABCMeta):
    """
    The ListABC provides the api for a basic list data structure
    """
    @abstractproperty
    def first(self):
        """
        Examine the element at the front of the list
        :return: element at front
        """
        pass

    @abstractproperty
    def last(self):
        """
        Examine the element at the rear of the list
        :return: element at rear
        """
        pass

    @abstractmethod
    def remove_first(self):
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

    @abstractproperty
    def is_empty(self):
        """
        Return True if list is empty, else False
        :return: True if empty, else False
        """
        pass

    @abstractproperty
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
class OrderedLinkedList(OrderedListABC):
    """
    The OrderedLinkedList class implements a linked list
    that will insert elements based on their ordering.
    It expects that elements are of the same type and
    order-comparable.
    An order-comparable class defines
        __eq__, __ne__, __lt__, __le__, __gt__, __ge__

    """
    def __init__(self, element_class):
        """
        :param element_class: class that this linked list will store
        """
        self.element_class = element_class
        self._list = LinkedList()

    def __iter__(self):
        for obj in self._list:
            yield obj

    def add(self, x):
        """
        Add an element into the list at its appropriate spot
        """
        if not isinstance(x, self.element_class):
            raise ListException("Cannot add element because is not an instance of {}"
                                .format(self.element_class.__name__))

        # find where the element belongs in the order
        # base case, empty list
        if len(self._list) == 0:
            self._list.insert_first(x)
        # > 0 element
        else:
            # loop until we hit a bigger item then insert
            prev_node = None
            node = self._list.first
            while node:
                if node.element > x:
                    break
                prev_node = node
                node = node.next_node

            if prev_node is None:
                # first item was greater than x
                self._list.insert_first(x)
            else:
                self._list.insert_after_node(prev_node, x)

        return

    @property
    def first(self):
        """
        Examine the element at the front of the list
        :return: element at front
        """
        # if there is nothing in the list then raise an exception
        if self.is_empty:
            raise ListException("Cannot fetch first element from empty list")
        return self._list.first.element

    @property
    def last(self):
        """
        Examine the element at the rear of the list
        :return: element at rear
        """
        # if there is nothing in the list then raise an exception
        if self.is_empty:
            raise ListException("Cannot fetch last element from empty list")
        return self._list.last.element

    def __len__(self):
        """
        Return the length of the list
        :return: number of elements
        """
        return len(self._list)

    @property
    def size(self):
        """
        Return the number of elements in the list
        :return:
        """
        return len(self._list)

    def remove_first(self):
        # if there is nothing in the list then raise an exception
        if self.is_empty:
            raise ListException("Cannot remove first from empty list")
        return self._list.delete_first()

    def remove_last(self):
        # if there is nothing in the list then raise an exception
        if self.is_empty:
            raise ListException("Cannot remove last from empty list")
        return self._list.delete_last()

    @property
    def is_empty(self):
        """
        Return true if list is empty else False
        :return: True or False
        """
        return True if self.size == 0 else False

    def contains(self, x):
        """
        Return True if list contains element x, else False
        :param x: object to check for
        :return: True if in list, else False
        """
        return self._list.search(x)
