import time


class BubbleSort:
    """
    This class is a python implementation of the problem discussed in this
    video by mycodeschool - https://www.youtube.com/watch?v=Jdtq5uKz-w4

    :Authors: pranaychandekar
    """

    @staticmethod
    def bubble_sort(unsorted_list: list):
        """
        This method sorts a given list in ascending order using Bubble Sort algorithm.

        :param unsorted_list: The list which needs to be sorted.
        :type unsorted_list: list
        """
        unsorted_list_size = len(unsorted_list)
        for i in range(unsorted_list_size - 1):
            all_sorted = True
            for j in range(unsorted_list_size - i - 1):
                if unsorted_list[j] > unsorted_list[j + 1]:
                    temp = unsorted_list[j]
                    unsorted_list[j] = unsorted_list[j + 1]
                    unsorted_list[j + 1] = temp
                    all_sorted = False
            if all_sorted:
                break


if __name__ == "__main__":
    tic = time.time()

    print("\nYou are currently running Bubble Sort test case.")

    unsorted_list = [2, 7, 4, 1, 5, 3]
    print("\nUnsorted List: ")
    for element in unsorted_list:
        print(str(element), end=", ")
    print()

    BubbleSort.bubble_sort(unsorted_list)

    print("\nSorted List: ")
    for element in unsorted_list:
        print(str(element), end=", ")
    print()

    toc = time.time()

    print("\nTotal time taken:", toc - tic, "seconds.")
