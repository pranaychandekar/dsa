import time


class CircularRotatedSortedArray:
    """
    This class is a python implementation of the problem discussed in the following videos by mycodeschool:
    1) No. of rotations - https://www.youtube.com/watch?v=4qjprDkJrjY
    2) Search element in circularly rotated array - https://www.youtube.com/watch?v=uufaK2uLnSI

    :Authors: pranaychandekar
    """

    @staticmethod
    def number_of_rotations(search_space: list):
        """
        This method performs a binary search on the sorted search space to find the number of circular rotations
        performed on the array.

        :param search_space: The sorted list of elements on which target needs to be searched.
        :type search_space: list
        :return: The index of the target.
        :rtype: int
        """
        search_space_size = len(search_space)
        start = 0
        end = search_space_size - 1

        while start <= end:
            if search_space[start] <= search_space[end]:
                return start

            mid = start + (end - start) // 2
            next = (mid + 1) % search_space_size
            previous = (mid + search_space_size - 1) % search_space_size

            if (
                search_space[previous] >= search_space[mid] <= search_space[next]
            ):  # Pivot property
                return mid
            elif search_space[mid] <= search_space[end]:
                end = mid - 1
            elif search_space[mid] >= search_space[start]:
                start = mid + 1

        return -1

    @staticmethod
    def search_target(search_space: list, target: int):
        """
        This method performs a binary search on the circularly rotated sorted search space to find the index of the
        target.

        :param search_space: The sorted list of elements on which target needs to be searched.
        :param target: The target to be located in the search space.
        :type search_space: list
        :type target: int
        :return: The index of the target.
        :rtype: int
        """
        search_space_size = len(search_space)

        start = 0
        end = search_space_size - 1

        while start <= end:
            mid = start + (end - start) // 2

            if search_space[mid] == target:
                return mid
            elif search_space[mid] <= search_space[end]:
                if search_space[mid] < target <= search_space[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif search_space[start] <= search_space[mid]:
                if search_space[start] <= target < search_space[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

        return -1


if __name__ == "__main__":
    tic = time.time()

    search_space = [9, 13, 14, 1, 4, 6, 7]
    target = 13

    print("\nSearch Space:", search_space)
    print("Target:", target)

    number_of_rotations = CircularRotatedSortedArray.number_of_rotations(search_space)

    print("\nThe search space is rotated", number_of_rotations, "times.")

    target_index = CircularRotatedSortedArray.search_target(search_space, target)

    if target_index == -1:
        print("\nThe target", target, "is not present in the search space.")
    else:
        print("\nThe target", target, "is at index", target_index)

    toc = time.time()

    print("\nTotal time taken:", toc - tic, "seconds.")
