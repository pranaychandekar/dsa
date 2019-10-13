import time


class TargetCount:
    """
    This class is a python implementation of the problem discussed in the following videos by mycodeschool:
    1) First or Last Occurrence - https://www.youtube.com/watch?v=OE7wUUpJw6I
    2) Target Count - https://www.youtube.com/watch?v=pLT_9jwaPLs

    :Authors: pranaychandekar
    """

    @staticmethod
    def find_occurrence(search_space: list, target: int, find_first: bool):
        """
        This method performs a binary search on the sorted search space to find the index of the target.
        Depending on the find_first boolean parameter it either the index of first occurrence or last occurrence.

        :param search_space: The sorted list of elements on which target needs to be searched.
        :param target: The target to be located in the search space.
        :param find_first: The flag to find the first occurrence.
        :type search_space: list
        :type target: int
        :type find_first: bool
        :return: The index of the target.
        :rtype: int
        """
        start = 0
        end = len(search_space) - 1

        target_index = -1

        while start <= end:
            mid = start + (end - start) // 2

            if search_space[mid] == target:
                target_index = mid
                if find_first:
                    end = mid - 1
                else:
                    start = mid + 1
            elif search_space[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return target_index

    @staticmethod
    def target_count(search_space: list, target: int):
        """
        This method returns the number of occurrences of a target element in a given sorted search space.

        :param search_space: The sorted list of elements on which target needs to be searched.
        :param target: The target to be located in the search space.
        :type search_space: list
        :type target: int
        :return: The count of occurrence of the target.
        :rtype: int
        """
        target_count = 0

        first_index = TargetCount.find_occurrence(search_space, target, True)

        if first_index != -1:
            last_index = TargetCount.find_occurrence(search_space, target, False)
            target_count = last_index - first_index + 1

        return target_count


if __name__ == "__main__":
    tic = time.time()

    search_space = [1, 4, 6, 6, 7, 9, 13, 13, 13, 14]
    target = 13

    print("\nSearch Space:", search_space)
    print("Target:", target)

    target_count = TargetCount.target_count(search_space, target)

    if target_count == 0:
        print("\nThe target:", target, "is not present in the given search space.")
    else:
        print("\nThe count of the target", target, ":", target_count)

    toc = time.time()

    print("\nTotal time taken:", toc - tic, "seconds.")
