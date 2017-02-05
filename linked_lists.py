"""
Implement linked list data structures
"""


class Node(object):
    """
    Represents a node in a linked list
    """
    def __init__(self, element=None):
        self._next_node = None
        self.element = element

    @property
    def next_node(self):
        """
        Next node connected to this node
        """
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        if next_node:
            if isinstance(next_node, Node):
                self._next_node = next_node
            else:
                # bad case. we only accept Nodes and Nones
                raise Exception("next_node must be Node instance or None")
        else:
            self._next_node = None

    def __str__(self):
        return "<Node object: {0}>".format(self.element, self.next_node)


class LinkedList(object):
    """
    Implements the LinkedList api to store objects in a linked list.
    Our linked list allows addition/removal of objects to the list.
    """
    def __init__(self):
        """
        --first: pointer to first Node
        --len: number of elements in list
        --last: pointer to last Node
        :return:
        """
        self.first = None
        self.len = 0
        self.last = None

    def __iter__(self):
        """
        Define iteration for the list, which is the traversal of each node
        Note: it is NOT a very good ideal to iterate and insert at the same time
        :return:
        """
        node = self.first
        while node:
            old_node = node
            node = old_node.next_node
            yield old_node.element

    def __len__(self):
        """
        Define the len function for this list, which is the number of nodes
        :return:
        """
        return self.len

    def insert_first(self, obj):
        """
        Add a node at the beginning of the
        linked list that contains this object
        :param: python object to insert
        :return:
        """
        node = Node(element=obj)
        old_first = self.first
        node.next_node = old_first
        self.first = node

        # very first entry, set self.first=Node, self.last=Node
        if old_first is None:
            self.last = self.first

        self.len += 1

    def _find_node(self, start_node, obj):
        """
        Find the node in the linked list
        :param obj: element of the node to find
        :return: node if it exists, else None
        """
        n = start_node
        found = None
        while n:
            if n.element == obj:
                found = n
                break
            else:
                n = n.next_node
        return found

    def insert_after_node(self, node, new_obj):
        """
        Insert the new obj after this node
        :param node: existing node
        :param new_obj: new element to add
        :return:
        """
        new_node = Node(element=new_obj)
        new_node.next_node = node.next_node
        node.next_node = new_node

        # move last pointer if at the end
        if new_node.next_node is None:
            self.last = new_node
            self.len += 1

        return

    def insert_after(self, obj, new_obj, occurrence=1):
        """
        Insert the new_obj after N occurrences of obj,
        where the default is after the first occurrence of obj (n=1)
        :param obj: current obj to find
        :param new_obj: new object to add
        :param occurrence: occurrence of obj to insert after
        :return:
        :raise: Exception if obj is not found
        """
        # find our node (1st, second, whatever)
        start_node = self.first
        current_node = None
        for i in range(0, occurrence):
            current_node = self._find_node(start_node, obj)
            start_node = current_node

        # insert new_obj
        if current_node:
            new_node = Node(element=new_obj)
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

            # move last pointer if at the end
            if new_node.next_node is None:
                self.last = new_node

            self.len += 1
        else:
            raise Exception("Cannot insert new_obj. No node found for obj.")

    def insert_last(self, obj):
        """
        Insert the obj at the end of the linked list
        :param obj: a python object
        :return:
        """
        new_node = Node(element=obj)

        n = self.first
        if n is None:
            n = Node(element=obj)
            self.first = n
            self.last = n
        else:
            while n.next_node:
                n = n.next_node
            n.next_node = new_node
            self.last = new_node
        self.len += 1

    def delete_first(self):
        """
        Delete the first element of the list.
        If length of list is None, leave as None.
        :return: deleted object
        """
        n = self.first

        if n:
            new_first = n.next_node
            self.first = new_first

            # update if empty
            if self.first is None:
                self.last = self.first

            self.len -= 1
        return n.element

    def delete_last(self):
        """
        Delete the last element of the list
        :return: deleted object
        """
        prev_node = None
        current_node = self.first

        if current_node:
            while current_node.next_node:
                prev_node = current_node
                current_node = current_node.next_node

            if prev_node:
                prev_node.next_node = None
                self.last = prev_node
            else:
                # we deleted the only node
                self.first = None
                self.last = None

            self.len -= 1
        return current_node.element

    def delete(self, obj):
        """
        Delete obj if it exists
        :param obj: python object to delete
        :return: deleted object
        :raise: Exception if obj not found
        """
        # find the ndoe
        prev_node = None
        current_node = self.first
        found = False
        while current_node:
            if current_node.element == obj:
                found = True
                break
            else:
                prev_node = current_node
                current_node = current_node.next_node

        # delete the node
        if found:
            if prev_node is None:
                # found first element of list
                self.first = current_node.next_node
            else:
                prev_node.next_node = current_node.next_node

            # found last element of list
            if current_node.next_node is None:
                self.last = prev_node

            current_node.next_node = None
            self.len -= 1
            return current_node.element
        else:
            raise Exception("Cannot delete obj. No node found for obj.")

    def search(self, obj):
        """
        Search for obj in the list
        :return: return True if exists, else False
        """
        n = self.first
        while n:
            if n.element == obj:
                return True
            n = n.next_node
        return False

    def size(self):
        """
        Return the size of the linked list
        :return:
        """
        return self.len


# TODO
class DoubleLinkedList(object):
    pass