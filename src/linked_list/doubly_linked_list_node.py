class DoublyLinkedListNode:
    """
        This class represents a node which can be used to create a Doubly Linked List.

        :Authors: pranaychandekar
        """

    def __init__(self, data, next=None, previous=None):
        """
        This method initializes a node for Doubly Linked List.

        :param data: The data to be stored in the node.
        :param next: The reference to the next node.
        :param previous: The reference to the previous node.
        """
        self.data = data
        self.next = next
        self.previous = previous

    def set_data(self, data):
        """
        This method sets the data in the Doubly Linked List node.

        :param data: The data in the node.
        """
        self.data = data

    def get_data(self):
        """
        This method returns the data in the Doubly Linked List node.

        :return: The data in the node.
        """
        return self.data

    def set_next(self, next):
        """
        This method sets the reference to the next node in the Doubly Linked List node.

        :param next: The reference to the next node.
        """
        self.next = next

    def get_next(self):
        """
        This method returns the reference to the next node in the Doubly Linked List node.

        :return: The reference to the next node.
        """
        return self.next

    def set_previous(self, previous):
        """
        This method sets the reference to the previous node in the Doubly Linked List node.

        :param previous: The reference to the previous node.
        """
        self.previous = previous

    def get_previous(self):
        """
        This method returns the reference to the previous node in the Doubly Linked List node.
        
        :return: The reference to the previous node.
        """
        return self.previous
