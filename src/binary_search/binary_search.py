import time


class BinarySearch:
    """
    This class is a python implementation of the problem discussed in the following videos by mycodeschool:
    1) Iterative - https://www.youtube.com/watch?v=OAZc1zwjERU
    2) Recursive - https://www.youtube.com/watch?v=-bQ4UzUmWe8

    :Authors: pranaychandekar
    """

    @staticmethod
    def binary_search_iterative(search_space: list, target: int):
        """
        This method performs a binary search on the sorted search space to find the index of the target.

        :param search_space: The sorted list of elements on which target needs to be searched.
        :param target: The target to be located in the search space.
        :type search_space: list
        :type target: int
        :return: The index of the target.
        :rtype: int
        """
        start = 0
        end = len(search_space) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if search_space[mid] == target:
                return mid
            elif search_space[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    def binary_search_recursive(
        self, search_space: list, target: int, start: int, end: int
    ):
        """
        This method performs a binary search on the sorted search space to find the index of the target using
        recursion technique.

        :param search_space: The sorted list of elements on which target needs to be searched.
        :param target: The target to be located in the search space.
        :param start: The start index.
        :param end: The end index.
        :type search_space: list
        :type target: int
        :type start: int
        :type end: int
        :return: The index of the target.
        :rtype: int
        """
        if start > end:
            return -1

        mid = start + (end - start) // 2

        if search_space[mid] == target:
            return mid
        elif search_space[mid] > target:
            return self.binary_search_recursive(search_space, target, start, mid - 1)
        else:
            return self.binary_search_recursive(search_space, target, mid + 1, end)


if __name__ == "__main__":
    tic = time.time()

    search_space = [1, 4, 6, 7, 9, 13, 14]
    target = 13

    print("\nSearch Space:", search_space)
    print("Target:", target)

    solution = BinarySearch()
    index_iterative = solution.binary_search_iterative(search_space, target)
    index_recursive = solution.binary_search_recursive(
        search_space, target, 0, len(search_space) - 1
    )

    assert index_iterative == index_recursive

    if index_iterative == -1:
        print("\nThe target:", target, "is not present in the given search space.")
    else:
        print(
            "\nThe target:",
            target,
            "is present at index",
            index_iterative,
            "in the given search space.",
        )

    toc = time.time()

    print("\nTotal time taken:", toc - tic, "seconds.")
