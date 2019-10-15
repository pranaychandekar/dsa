import time


class Queues:
    """
    This class is an implementation of a Queue data structure.

    :Authors: pranaychandekar
    """

    def __init__(self):
        """
        This method initializes a Queue.
        """
        self.queue = []

    def enqueue(self, data):
        """
        This method adds a data point to the Queue.

        :param data: The data to be enqueued.
        """
        self.queue.append(data)

    def de_queue(self):
        """
        This method removes the first data point in the Queue and returns the same.

        :return: The first data point.
        """
        front = None
        if self.is_empty():
            print("Queue is empty!")
        else:
            front = self.queue[0]
            self.queue = self.queue[1:]
        return front

    def front(self):
        """
        This method returns the first data point in the Queue.

        :return: The first data point.
        """
        front = None
        if self.is_empty():
            print("Queue is empty!")
        else:
            front = self.queue[0]
        return front

    def is_empty(self):
        """
        This method checks whether a given Queue is empty and returns a boolean flag accordingly.

        :return: The boolean flag indicating the Queue empty status.
        """
        return self.size() == 0

    def size(self):
        """
        This method returns the current size of the Queue.

        :return: The size.
        """
        return len(self.queue)


if __name__ == "__main__":
    tic = time.time()

    queue = Queues()
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(8)
    queue.enqueue(13)
    queue.enqueue(21)

    print("\nThe length of the queue is", queue.size())

    print("\nThe first element in the queue:", queue.front())

    queue.de_queue()

    while not queue.is_empty():
        print("\nThe front element in queue after de queue", queue.de_queue())

    toc = time.time()

    print("\nTotal time taken", toc - tic, "seconds.")
