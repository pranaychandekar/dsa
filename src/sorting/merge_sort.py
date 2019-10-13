import time


class MergeSort:
    """
    This class is a python implementation of the problem discussed in this
    video by mycodeschool - https://www.youtube.com/watch?v=TzeBrDU-JaY

    :Authors: pranaychandekar
    """

    @staticmethod
    def merge(left: list, right: list, original: list):
        """
        This method implements the merge logic to merge two halves of a list.

        :param left: The left half of the original list.
        :param right: The right half of the original list.
        :param original: The original list.
        :type left: list
        :type right: list
        :type original: list
        """
        left_length = len(left)
        right_length = len(right)

        left_pointer = right_pointer = original_pointer = 0

        while left_pointer < left_length and right_pointer < right_length:
            if left[left_pointer] <= right[right_pointer]:
                original[original_pointer] = left[left_pointer]
                left_pointer = left_pointer + 1
            else:
                original[original_pointer] = right[right_pointer]
                right_pointer = right_pointer + 1
            original_pointer = original_pointer + 1

        if left_pointer < left_length:
            original[original_pointer:] = left[left_pointer:]

        if right_pointer < right_length:
            original[original_pointer:] = right[right_pointer:]

    def merge_sort(self, unsorted_list: list):
        """
        This method sorts a given list in ascending order using Merge Sort algorithm.

        :param unsorted_list: The list which needs to be sorted.
        :type unsorted_list: list
        """
        unsorted_list_size = len(unsorted_list)

        if unsorted_list_size < 2:
            return

        mid = int(unsorted_list_size / 2)
        left = unsorted_list[0:mid]
        right = unsorted_list[mid:]

        self.merge_sort(left)
        self.merge_sort(right)
        self.merge(left, right, unsorted_list)


if __name__ == "__main__":
    tic = time.time()

    print("\nYou are currently running Merge Sort test case.")

    unsorted_list = [2, 7, 4, 1, 5, 3]
    print("\nUnsorted List: ")
    for element in unsorted_list:
        print(str(element), end=", ")
    print()

    solution = MergeSort()
    solution.merge_sort(unsorted_list)

    print("\nSorted List: ")
    for element in unsorted_list:
        print(str(element), end=", ")
    print()

    toc = time.time()

    print("\nTotal time taken:", toc - tic, "seconds.")
