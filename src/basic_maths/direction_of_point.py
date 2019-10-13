import time


class DirectionOfPoint:
    """
    This class is a python implementation of the problem discussed in this
    video by mycodeschool - https://www.youtube.com/watch?v=VMVuKpj_RQQ

    :Authors: pranaychandekar
    """

    @staticmethod
    def cross_product(a: tuple, b: tuple):
        """
        This method returns cross product of two vectors A and B.

        :param a: Point A
        :param b: Point B
        :type a: tuple
        :type b: tuple
        :return: Cross Product of vector A and vector B
        :rtype: float
        """
        return a[0] * b[1] - b[0] * a[1]

    @staticmethod
    def shift_origin(old_point: tuple, new_origin: tuple):
        """
        This method returns the new co-ordinates for an existing point w.r.t new origin.

        :param old_point: Existing location in cartesian plane
        :param new_origin: The new origin for the cartesian plane
        :type old_point: tuple
        :type new_origin: tuple
        :return: New co-ordinates for old_point w.r.t new_origin
        ;:rtype: tuple
        """
        return old_point[0] - new_origin[0], old_point[1] - new_origin[1]

    def get_direction(self, a: tuple, b: tuple, p: tuple):
        b = self.shift_origin(b, a)
        p = self.shift_origin(p, a)

        cross_product_value = self.cross_product(b, p)

        if cross_product_value > 0:
            return "left"
        elif cross_product_value < 0:
            return "right"
        else:
            return "line"


if __name__ == "__main__":
    tic = time.time()

    a = (-20, -20)
    b = (3, 3)

    # p = (2, 4)  # This is on left
    # p = (2, 1)  # This is on right
    p = (2, 2)  # This is on the line

    solution = DirectionOfPoint()

    print(
        "\nThe point P",
        p,
        "is on the",
        solution.get_direction(a, b, p),
        "of segment A",
        a,
        "to B",
        b,
    )

    toc = time.time()

    print("\nTotal time taken", toc - tic, "seconds.")
