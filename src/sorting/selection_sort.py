import time


class SelectionSort:
    """
    This class is a python implementation of the problem discussed in this
    video by mycodeschool - https://www.youtube.com/watch?v=GUDLRan2DWM

    :Authors: pranaychandekar
    """

    @staticmethod
    def selection_sort(unsorted_list: list):
        """
        This method sorts a given list in ascending order using Selection Sort algorithm.

        :param unsorted_list: The list which needs to be sorted.
        :type unsorted_list: list
        """
        unsorted_list_size = len(unsorted_list)
        for i in range(unsorted_list_size - 1):
            minimum_element_index = i
            j = i + 1
            while j < unsorted_list_size:
                if unsorted_list[j] < unsorted_list[minimum_element_index]:
                    minimum_element_index = j
                j = j + 1
            temp = unsorted_list[i]
            unsorted_list[i] = unsorted_list[minimum_element_index]
            unsorted_list[minimum_element_index] = temp


if __name__ == "__main__":
    tic = time.time()

    print("\nYou are currently running Selection Sort test case.")

    unsorted_list = [2, 7, 4, 1, 5, 3]
    print("\nUnsorted List: ")
    for element in unsorted_list:
        print(str(element), end=", ")
    print()

    SelectionSort.selection_sort(unsorted_list)

    print("\nSorted List: ")
    for element in unsorted_list:
        print(str(element), end=", ")
    print()

    toc = time.time()
    
    print("\nTotal time taken:", toc - tic, "seconds.")
