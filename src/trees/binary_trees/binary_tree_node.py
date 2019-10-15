class BinaryTreeNode:
    """
    This class represents a node which can be used to create a Binary Tree.

    :Authors: pranaychandekar
    """

    def __init__(self, data, left=None, right=None, parent=None):
        """
        This method initializes a node for Binary Tree.

        :param data: The data to be stored in the node.
        :param left: The reference to the left child.
        :param right: The reference to the right child.
        :param parent: The reference to the parent which can be used for reverse traversal.
        """
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def set_data(self, data):
        """
        This method sets the data in the Binary Tree node.

        :param data: The data in the node.
        """
        self.data = data

    def get_data(self):
        """
        This method returns the data in the Binary Tree node.

        :return: The data in the node.
        """
        return self.data

    def has_data(self):
        """
        This method returns a boolean flag indicating the presence of data in the node.

        :return: The boolean flag validating the presence of the data in the node.
        """
        return self.data is not None

    def set_left(self, left):
        """
        This method sets the left child of the Binary Tree node.

        :param left: The reference to the left child.
        """
        self.left = left

    def get_left(self):
        """
        This method returns the left child of the Binary Tree node.

        :return: The reference to the left child.
        """
        return self.left

    def has_left(self):
        """
        This method returns the boolean flag indicating the presence of a left child in the node.

        :return: The boolean flag validating the presence of the left child in the node.
        """
        return self.left is not None

    def set_right(self, right):
        """
        This method sets the right child of the Binary Tree node.

        :param right: The reference to the right child.
        """
        self.right = right

    def get_right(self):
        """
        This method returns the right child of the Binary Tree node.

        :return: The reference to the right child.
        """
        return self.right

    def has_right(self):
        """
        This method returns the boolean flag indicating the presence of a right child in the node.

        :return: The boolean flag validating the presence of the right child in the node.
        """
        return self.right is not None

    def set_parent(self, parent):
        """
        This method sets the parent of the Binary Tree node.

        :param parent: The reference to the parent.
        """
        self.parent = parent

    def get_parent(self):
        """
        This method returns the parent of the Binary Tree node.

        :return: The reference to the parent.
        """
        return self.parent

    def has_parent(self):
        """
        This method returns the boolean flag indicating the presence of a parent in the node.

        :return: The boolean flag indicating the presence of the parent of the node.
        """
        return self.parent is not None
