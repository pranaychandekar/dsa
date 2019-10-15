import time

from trees.binary_trees.binary_tree import BinaryTree
from trees.binary_trees.binary_tree_node import BinaryTreeNode


class BinarySearchTree(BinaryTree):
    """
    This class is dynamic node implementation of a Binary Search Tree(BST).

    For more details check out the below links by mycodeschool:
    1) Binary Search Tree - https://www.youtube.com/watch?v=pYT9F8_LFTM
    2) Implementation - Insert and Search - https://www.youtube.com/watch?v=COZK7NATh4k
    3) Implementation - Remove - https://www.youtube.com/watch?v=gcULXE7ViZw
    4) Is Binary Tree a BST - https://www.youtube.com/watch?v=yEwSGhSsT0U
    5) Get min and max in BST - https://www.youtube.com/watch?v=Ut90klNN264

    :Authors: pranaychandekar
    """

    def __init__(self, root_data):
        """
        This method initializes the BST object with the root data.

        :param root_data: The data to be inserted at the root node of the BST.
        """
        super(BinarySearchTree, self).__init__(root_data)

    def insert(self, current: BinaryTreeNode, data, parent=None, add_parent=False):
        """
        This method inserts a new data node in the BST using recursion.

        :param current: The current node.
        :param data: The data to be inserted.
        :param parent: The parent for the new node.
        :param add_parent: The flag to add parent.
        :return: The tree with the new data node.
        """
        if current is None:
            return BinaryTreeNode(data, parent=parent)
        elif data <= current.get_data():
            current.set_left(self.insert(current.get_left(), data, current, add_parent))
        elif current.get_data() < data:
            current.set_right(
                self.insert(current.get_right(), data, current, add_parent)
            )
        return current

    def search(self, current: BinaryTreeNode, search_target):
        """
        This method tells whether a given data point is there in the BST.

        :param current: The current node.
        :param search_target: The data to be searched.
        :return: The boolean flag whether the data is present.
        """
        if current is None:
            return False
        elif current.get_data() == search_target:
            return True
        elif search_target <= current.get_data():
            return self.search(current.get_left(), search_target)
        else:
            return self.search(current.get_right(), search_target)

    def remove(self, current: BinaryTreeNode, to_remove):
        """
        This method removes the data node from the BST if the data is present.

        todo - how to update parents?

        :param current: The current node.
        :param to_remove: The data to be removed from BST.
        :return: The updated current node.
        """
        if current is None:
            return current
        elif to_remove < current.get_data():
            current.set_left(self.remove(current.get_left(), to_remove))
        elif current.get_data() < to_remove:
            current.set_right(self.remove(current.get_right(), to_remove))
        else:
            if not current.has_left() and not current.has_right():
                current = None
            elif not current.has_left():
                current = current.get_right()
            elif not current.has_right():
                current = current.get_left()
            else:
                current.set_data(self.get_min(current.get_right()))
                current.set_right(self.remove(current.get_right(), current.get_data()))
        return current

    @staticmethod
    def is_bst(current: BinaryTreeNode, min_val=float("-inf"), max_val=float("inf")):
        """
        This method checks whether a given Binary Tree is a BST.

        :param current: The current node.
        :param min_val: The minimum value which should be less than or equal to the current node data to be a BST.
        :param max_val: The maximum value which should be greater than or equal to the current node data to be a BST.
        :return: The boolean flag indicating whether the given Binary Tree is a BST.
        """
        if current is None:
            return True

        if (
            min_val <= current.get_data() <= max_val
            and BinarySearchTree.is_bst(current.get_left(), min_val, current.get_data())
            and BinarySearchTree.is_bst(
                current.get_right(), current.get_data(), max_val
            )
        ):
            return True

        return False

    @staticmethod
    def get_min(current: BinaryTreeNode):
        """
        This method returns the minimum value in a BST.

        :param current: The current node.
        :return: The minimum value in the BST
        """
        while current.has_left():
            current = current.get_left()
        return current.get_data()

    @staticmethod
    def get_max(current: BinaryTreeNode):
        """
        This method returns the maximum value in a BST.

        :param current: The current node.
        :return: The maximum value in the BST
        """
        while current.has_right():
            current = current.get_right()
        return current.get_data()


if __name__ == "__main__":
    tic = time.time()

    bst = BinarySearchTree(15)

    bst.set_root(bst.insert(bst.get_root(), 15))
    bst.set_root(bst.insert(bst.get_root(), 10))
    bst.set_root(bst.insert(bst.get_root(), 25))
    bst.set_root(bst.insert(bst.get_root(), 9))
    bst.set_root(bst.insert(bst.get_root(), 3))
    bst.set_root(bst.insert(bst.get_root(), 21))

    from trees.binary_trees.binary_tree_traversal import BinaryTreeTraversal

    result = list()
    BinaryTreeTraversal.in_order(bst.get_root(), result)

    if BinarySearchTree.is_bst(bst.get_root()):
        print("\nThe tree", result, "is a valid BST.")
    else:
        print("\nThe tree", result, "is an invalid BST.")

    print("\nThe height of the current tree is", BinaryTree.get_height(bst.get_root()))

    print(
        "\nThe minimum value in the tree is", BinarySearchTree.get_min(bst.get_root())
    )

    print(
        "\nThe maximum value in the tree is", BinarySearchTree.get_max(bst.get_root())
    )

    search_target = 21
    is_data_in_bst = bst.search(bst.get_root(), search_target)

    if is_data_in_bst:
        print(
            "\nThe data point", search_target, "is present in the Binary Search Tree."
        )
    else:
        print(
            "\nThe data point",
            search_target,
            "was not found in the Binary Search Tree.",
        )

    to_remove = 15
    bst.set_root(bst.remove(bst.get_root(), to_remove))
    result = list()
    BinaryTreeTraversal.in_order(bst.get_root(), result)
    print("\nThe tree after removing", to_remove, ":", result)

    toc = time.time()

    print("\nTotal time taken", toc - tic, "seconds.")
