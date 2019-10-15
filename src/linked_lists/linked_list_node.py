class LinkedListNode:
    """
    This class represents a node which can be used to create a Linked List.

    :Authors: pranaychandekar
    """

    def __init__(self, data=None, next=None):
        """
        This method initializes a node for Linked List.

        :param data: The data to be stored in the node.
        :param next: The reference to the next node.
        """
        self.data = data
        self.next = next

    def set_data(self, data):
        """
        This method sets the data in the Linked List node.

        :param data: The data in the node.
        """
        self.data = data

    def get_data(self):
        """
        This method returns the data in the Linked List node.

        :return: The data in the node.
        """
        return self.data

    def has_data(self):
        """
        This method returns the boolean flag indicating the presence of data in the node.

        :return: The boolean flag validating the presence of the data in the node.
        """
        return self.data is not None

    def set_next(self, next):
        """
        This method sets the reference to the next node in the Linked List node.

        :param next: The reference to the next node.
        """
        self.next = next

    def get_next(self):
        """
        This method returns the reference to the next node in the Linked List node.

        :return: The reference to the next node.
        """
        return self.next

    def has_next(self):
        """
        This method returns the boolean flag indicating the presence of a next node.

        :return: The boolean flag validating the presence of the next node.
        """
        return self.next is not None
