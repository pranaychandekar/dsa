import time

from linked_lists.linked_list_node import LinkedListNode


class LinkedList:
    """
    This class is an implementation of a Linked List data structure.

    For more details please refer to these amazing videos by mycodeschool:
    1) Linked List
        a) Introduction - https://www.youtube.com/watch?v=NobHlGUjV3g
        b) Linked List vs Arrays - https://www.youtube.com/watch?v=lC-yYCOnN8Q
    2) Implementation - https://www.youtube.com/watch?v=vcQIFT79_50
    3) Insert a node
        a) At the beginning - https://www.youtube.com/watch?v=cAZ8CyDY56s
        b) At nth position - https://www.youtube.com/watch?v=IbvsNF22Ud0
    4) Delete a node at nth position - https://www.youtube.com/watch?v=Y0n86K43GO4
    5) Traverse - https://www.youtube.com/watch?v=K7J3nCeRC80
    6) Reverse
        a) Iterative - https://www.youtube.com/watch?v=sYcOK51hl-A
        b) Recursive - https://www.youtube.com/watch?v=KYH83T4q6Vs

    :Authors: pranaychandekar
    """

    def __init__(self):
        """
        This method initializes an instance of a Linked List.
        """
        self.head = LinkedListNode()

    def set_head(self, head: LinkedListNode):
        """
        This method sets the head of the Linked List.

        :param head: The new head.
        """
        self.head = head

    def get_head(self):
        """
        This method returns the head of the Linked List.

        :return: The head of the Linked List.
        """
        return self.head

    @staticmethod
    def size(current: LinkedListNode):
        """
        This method returns the size of the Linked List from the given node.

        :param current: The node from which size of the remaining list is to be computed.
        :return: The size of the list.
        """
        size = 0

        if current is not None:
            size += 1

        while current.has_next():
            size += 1
            current = current.get_next()

        return size

    def insert(self, data, position: int):
        """
        This method inserts an element at the position passed as the parameter.

        :param data: The data in the new node.
        :param position: The position of the new node.
        """
        if position == 0:
            if self.head.has_next():
                self.set_head(LinkedListNode(data, self.get_head()))
            else:
                self.set_head(LinkedListNode(data))

        elif position <= self.size(self.head):
            counter = 0
            current = self.get_head()
            while counter < position - 1:
                counter += 1
                current = current.get_next()
            current.set_next(LinkedListNode(data, current.get_next()))

        else:
            raise IndexError

    def remove(self, position: int):
        """
        This method removes the element from the position passed as the parameter.

        :param position: The position of the element to be removed.
        """
        if position == 0:
            self.set_head(self.get_head().get_next())

        elif position < self.size(self.head):
            counter = 0
            current = self.get_head()
            while counter < position - 1:
                current = current.get_next()
                counter += 1
            current.set_next(current.get_next().get_next())

        else:
            raise IndexError

    @staticmethod
    def traverse(current: LinkedListNode):
        """
        This method traverses a Linked List from a given node.

        :param current: The current node.
        :return: The result of the traverse.
        """
        result = []

        if current is not None:
            result.append(current.get_data())
            while current.has_next():
                current = current.get_next()
                result.append(current.get_data())

        return result

    def reverse(self):
        """
        This method reverses the given Linked List.
        """
        if self.get_head() is not None and self.get_head().has_next():
            current = self.get_head()
            previous = None
            next = current.get_next()
            while current.has_next():
                current.set_next(previous)
                previous = current
                current = next
                next = current.get_next()
            current.set_next(previous)
            self.set_head(current)

    @staticmethod
    def traverse_recursive(current: LinkedListNode, result: list):
        """
        This method traverses a Linked List using the recursion technique.

        :param current: The current node.
        :param result: The list which collects the result of the traversal.
        """
        if current is None:
            return
        result.append(current.get_data())
        LinkedList.traverse_recursive(current.get_next(), result)

    def reverse_recursive(self, current: LinkedListNode = None, previous=None):
        """
        This method reverses the Linked List using recursion technique.

        :param current: The current node.
        :param previous: The previous node.
        """
        if current is None:
            current = self.get_head()
        if current.has_next():
            next = current.get_next()
            current.set_next(previous)
            self.reverse_recursive(next, current)
        else:
            current.set_next(previous)
            self.set_head(current)

    @staticmethod
    def is_looped():
        pass

    @staticmethod
    def loop_position():
        pass


if __name__ == "__main__":
    tic = time.time()

    head_position = 0

    linked_list = LinkedList()

    linked_list.insert(0, head_position)
    linked_list.insert(1, 1)
    linked_list.insert(1, 2)
    linked_list.insert(2, 3)
    linked_list.insert(3, 4)
    linked_list.insert(5, 5)
    linked_list.insert(8, 6)

    print("\nThe new list:", LinkedList.traverse(linked_list.get_head()))

    new_head_data = 13
    linked_list.insert(new_head_data, head_position)
    print(
        "\nThe list after adding data",
        new_head_data,
        "at head:",
        LinkedList.traverse(linked_list.get_head()),
    )

    random_position = 2
    new_node_data = 21
    linked_list.insert(new_node_data, random_position)
    print(
        "\nThe list after adding data",
        new_node_data,
        "at position",
        random_position,
        ":",
        LinkedList.traverse(linked_list.get_head()),
    )

    remove_position = 2
    linked_list.remove(remove_position)
    print(
        "\nThe list after removing data at position",
        remove_position,
        ":",
        LinkedList.traverse(linked_list.get_head()),
    )

    remove_position = 0
    linked_list.remove(remove_position)
    print(
        "\nThe list after removing data at position",
        remove_position,
        ":",
        LinkedList.traverse(linked_list.get_head()),
    )

    linked_list.reverse_recursive()
    result = list()
    LinkedList.traverse_recursive(linked_list.get_head(), result)
    print("\nThe list after reversing", result)

    toc = time.time()

    print("\nTotal time taken", toc - tic, "seconds.")
