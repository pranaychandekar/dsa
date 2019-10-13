import time


class InsertionSort:
    """
    This class is a python implementation of the problem discussed in this
    video by mycodeschool - https://www.youtube.com/watch?v=i-SKeOcBwko

    :Authors: pranaychandekar
    """

    @staticmethod
    def insertion_sort(unsorted_list: list):
        """
        This method sorts a given list in ascending order using Insertion Sort algorithm.

        :param unsorted_list: The list which needs to be sorted.
        :type unsorted_list: list
        """
        unsorted_list_size = len(unsorted_list)
        for i in range(1, unsorted_list_size):
            empty_block_original_value = unsorted_list[i]
            empty_block = i
            while (
                empty_block > 0
                and unsorted_list[empty_block - 1] > empty_block_original_value
            ):
                unsorted_list[empty_block] = unsorted_list[empty_block - 1]
                empty_block = empty_block - 1
            unsorted_list[empty_block] = empty_block_original_value


if __name__ == "__main__":
    tic = time.time()

    print("\nYou are currently running Insertion Sort test case.")

    unsorted_list = [2, 7, 4, 1, 5, 3]
    print("\nUnsorted List: ")
    for element in unsorted_list:
        print(str(element), end=", ")
    print()

    InsertionSort.insertion_sort(unsorted_list)
    print("\nSorted List: ")
    for element in unsorted_list:
        print(str(element), end=", ")
    print()

    toc = time.time()

    print("\nTotal time taken:", toc - tic, "seconds.")
