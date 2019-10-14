from src.trees.binary_trees.binary_tree_node import BinaryTreeNode


class BinaryTree:
    """
    This is an abstract class for a Binary Tree.
    For more details, please refer to this awesome explanation by mycodeschool:
    1) Binary Tree - https://www.youtube.com/watch?v=H5JubkIy_p8
    2) Height of a Binary Tree - https://www.youtube.com/watch?v=_pnqMz5nrRs

    :Authors: pranaychandekar
    """

    def __init__(self, root_data):
        """
        This method initializes a Binary Tree object with the root data.

        :param root_data: The data at the root node of th Binary Tree.
        """
        self.root = BinaryTreeNode(root_data)

    def set_root(self, root: BinaryTreeNode):
        """
        This method sets the root of the Binary Tree.

        :param root: The reference to the new root.
        """
        self.root = root

    def get_root(self):
        """
        This method returns the root of the Binary Tree.

        :return: The reference to the current root of the Binary Tree.
        """
        return self.root

    def insert(self, current: BinaryTreeNode, data):
        """
        This is an abstract method for inserting the data in the Binary Tree.

        :param current: The current node.
        :param data: The data to be inserted.
        :return: The reference to the current node.
        """
        pass

    def search(self, current: BinaryTreeNode, search_target):
        """
        This is an abstract method for verifying the presence of a data point in the Binary Tree.

        :param current: The current node.
        :param search_target: The data to be searched.
        :return: The boolean flag whether the data is present.
        """
        pass

    def remove(self, current: BinaryTreeNode, data):
        """
        This is an abstract method for removing a data point from the Binary Tree.

        :param current: The current node.
        :param data: The data to be removed.
        :return: The updated current node.
        """
        pass

    @staticmethod
    def get_height(current: BinaryTreeNode):
        """
        This method computes the height of a Binary Tree.

        :param current: The current node from where we want to find the height.
        :return: The height of the current node.
        """
        if current is None:
            return -1
        return 1 + max(
            BinaryTree.get_height(current.get_left()),
            BinaryTree.get_height(current.get_right()),
        )
