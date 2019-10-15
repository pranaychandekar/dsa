import time

from trees.binary_trees.binary_tree_node import BinaryTreeNode
from queues.queues import Queues


class BinaryTreeTraversal:
    """
    This class implements the solution to the problems discussed in the following videos by mycodeschool:

    1) Binary Tree Traversal - https://www.youtube.com/watch?v=9RHO6jU--GU
    2) Breadth First - Level Order - https://www.youtube.com/watch?v=86g8jAQug04
    3) Depth First - Pre-order, In-order and Post-order - https://www.youtube.com/watch?v=gm8DUJJhmY4

    :Authors: pranaychandekar
    """

    @staticmethod
    def level_order(current: BinaryTreeNode, result: list):
        """
        This method implements the Breadth First - Level Order Traversal of a Binary Tree.

        :param current: The current node in the tree.
        :param result: The list to collect the result of the traversal.
        """
        if current is None:
            return

        queue = Queues()
        queue.enqueue(current)

        while not queue.is_empty():
            current = queue.de_queue()

            result.append(current.get_data())

            if current.get_left() is not None:
                queue.enqueue(current.get_left())

            if current.get_right() is not None:
                queue.enqueue(current.get_right())

    @staticmethod
    def pre_order(current: BinaryTreeNode, result: list):
        """
        This method implements the Depth First - Pre-order Traversal of a Binary Tree.

        :param current: The current node in the tree.
        :param result: The list to collect the result of the traversal.
        """
        if current is None:
            return
        result.append(current.get_data())
        BinaryTreeTraversal.pre_order(current.get_left(), result)
        BinaryTreeTraversal.pre_order(current.get_right(), result)

    @staticmethod
    def in_order(current: BinaryTreeNode, result: list):
        """
        This method implements the Depth First - In-order Traversal of a Binary Tree.

        :param current: The current node in the tree.
        :param result: The list to collect the result of the traversal.
        """
        if current is None:
            return
        BinaryTreeTraversal.in_order(current.get_left(), result)
        result.append(current.get_data())
        BinaryTreeTraversal.in_order(current.get_right(), result)

    @staticmethod
    def post_order(current: BinaryTreeNode, result: list):
        """
        This method implements the Depth First - Post-order Traversal of a Binary Tree.

        :param current: The current node in the tree.
        :param result: The list to collect the result of the traversal.
        """
        if current is None:
            return
        BinaryTreeTraversal.post_order(current.get_left(), result)
        BinaryTreeTraversal.post_order(current.get_right(), result)
        result.append(current.get_data())


if __name__ == "__main__":
    tic = time.time()

    from trees.binary_trees.binary_search_trees.binary_search_tree import (
        BinarySearchTree,
    )

    bst = BinarySearchTree(15)

    bst.set_root(bst.insert(bst.get_root(), 15))
    bst.set_root(bst.insert(bst.get_root(), 10))
    bst.set_root(bst.insert(bst.get_root(), 25))
    bst.set_root(bst.insert(bst.get_root(), 9))
    bst.set_root(bst.insert(bst.get_root(), 3))
    bst.set_root(bst.insert(bst.get_root(), 21))

    result = list()
    BinaryTreeTraversal.level_order(bst.get_root(), result)
    print("\nLevel order Traversal", result)

    result = list()
    BinaryTreeTraversal.pre_order(bst.get_root(), result)
    print("\nPre-order Traversal", result)

    result = list()
    BinaryTreeTraversal.in_order(bst.get_root(), result)
    print("\nIn-order Traversal", result)

    result = list()
    BinaryTreeTraversal.post_order(bst.get_root(), result)
    print("\nPost-order Traversal", result)

    toc = time.time()

    print("\nTotal time taken", toc - tic, "seconds.")
