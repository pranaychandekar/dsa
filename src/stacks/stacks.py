import time


class Stacks:
    """
    This class is an implementation of a Stack data structure.

    :Authors: pranaychandekar
    """

    def __init__(self):
        """
        This method initializes a Stack.
        """
        self.stack: list = []

    def push(self, data):
        """
        This method adds a data point to the Stack.

        :param data: The data to be stacked.
        """
        self.stack.append(data)

    def pop(self):
        """
        This method removes the first data point in the Stack and returns the same.

        :return: The top data point.
        """
        top = None
        if self.is_empty():
            print("Stack is empty!")
        else:
            top = self.stack.pop()
        return top

    def top(self):
        """
        This method returns the first data point in the Stack.

        :return: The first data point.
        """
        top = None
        if self.is_empty():
            print("Stack is empty!")
        else:
            top = self.stack[-1]
        return top

    def is_empty(self):
        """
        This method checks whether a given Stack is empty and returns a boolean flag accordingly.

        :return: The boolean flag indicating the Stack empty status.
        """
        return self.size() == 0

    def size(self):
        """
        This method returns the current size of the Stack.

        :return: The size.
        """
        return len(self.stack)


if __name__ == "__main__":
    tic = time.time()

    stack = Stacks()
    stack.push(0)
    stack.push(1)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(5)
    stack.push(8)
    stack.push(13)
    stack.push(21)

    print("\nThe size of the stack is", stack.size())

    print("\nThe top element in the stack:", stack.top())

    stack.pop()

    while not stack.is_empty():
        print("\nThe top element in stack after pop", stack.pop())

    toc = time.time()

    print("\nTotal time taken", toc - tic, "seconds.")
