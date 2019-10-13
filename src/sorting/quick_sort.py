import time
import random


class QuickSort:
    """
    This class is a python implementation of the problem discussed in this
    video by mycodeschool - https://www.youtube.com/watch?v=COk73cpQbFQ

    :Authors: pranaychandekar
    """

    @staticmethod
    def swap(index1: int, index2: int, array_list: list):
        """
        This method swaps elements in a list corresponding to indexes given in parameters.

        :param index1: The first index.
        :param index2: The second index.
        :param array_list: The list in which we need to swap elements.
        :type index1: int
        :type index2: int
        :type array_list: list
        """
        temp = array_list[index1]
        array_list[index1] = array_list[index2]
        array_list[index2] = temp

    def partition(self, start: int, end: int, array_list: list):
        """
        This method creates partition in the list corresponding to the pivot element and return the pivot index.

        :param start: The start index.
        :param end: The end index
        :param array_list: The list of numbers.
        :type start: int
        :type end: int
        :type array_list: list
        :return: The partition pivot index
        :rtype: int
        """
        pivot = array_list[end]

        partition_index = start

        for i in range(start, end):
            if array_list[i] <= pivot:
                self.swap(i, partition_index, array_list)
                partition_index = partition_index + 1

        self.swap(partition_index, end, array_list)

        return partition_index

    def random_partition(self, start: int, end: int, unsorted_list: list):
        """
        This method randomly picks the pivot index and then swaps it with the last index before partitioning to
        avoid the worst case time complexity.

        :param start: The start index.
        :param end: The end index
        :param unsorted_list: The original list.
        :type start: int
        :type end: int
        :type unsorted_list: list
        :return: The partition pivot index.
        :rtype: int
        """
        pivot_index = random.randint(start, end)

        self.swap(pivot_index, end, unsorted_list)

        return self.partition(start, end, unsorted_list)

    def quick_sort(self, start: int, end: int, unsorted_list: list):
        """
        This method sorts a given list in ascending order using Quick Sort algorithm.

        :param start: The start index.
        :param end: The end index
        :param unsorted_list: The original list.
        :type start: int
        :type end: int
        :type unsorted_list: list
        """
        if start < end:
            partition_index = self.random_partition(start, end, unsorted_list)
            self.quick_sort(start, partition_index - 1, unsorted_list)
            self.quick_sort(partition_index + 1, end, unsorted_list)


if __name__ == "__main__":
    tic = time.time()

    print("\nYou are currently running Quick Sort test case.")

    unsorted_list = [7, 2, 1, 6, 8, 5, 3, 4]
    print("\nUnsorted List: ")
    for element in unsorted_list:
        print(str(element), end=", ")
    print()

    solution = QuickSort()
    solution.quick_sort(0, len(unsorted_list) - 1, unsorted_list)

    print("\nSorted List: ")
    for element in unsorted_list:
        print(str(element), end=", ")
    print()

    toc = time.time()

    print("\nTotal time taken:", toc - tic, "seconds.")
