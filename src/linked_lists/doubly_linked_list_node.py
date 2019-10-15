from linked_lists.linked_list_node import LinkedListNode


class DoublyLinkedListNode(LinkedListNode):
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
        super(LinkedListNode, self).__init__(data, next)
        self.previous = previous

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
