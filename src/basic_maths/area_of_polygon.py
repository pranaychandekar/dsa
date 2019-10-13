import time


class AreaOfPolygon:
    """
    This class is a python implementation of the problem discussed in this
    video by mycodeschool - https://www.youtube.com/watch?v=WAyPIMme3Yw

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

    def area_of_polygon(self, points: list):
        """
        This method returns area of a polygon in a cartesian plane.

        :param points: The list of points of polygon in clockwise or counter clockwise
        :type points: list of tuples
        :return: The area of polygon formed by points.
        :rtype: float
        """
        area_of_polygon = 0

        for i in range(len(points)):
            area_of_polygon += self.cross_product(
                points[i], points[(i + 1) % len(points)]
            )

        return abs(area_of_polygon) / 2


if __name__ == "__main__":
    tic = time.time()

    points = [
        (3, 1),
        (2, 3),
        (0, 0),
    ]  # Enter the points as tuple in either clockwise or counter-clockwise order

    solution = AreaOfPolygon()
    area_of_polygon = solution.area_of_polygon(points)

    print("\nArea of polygon is", area_of_polygon)

    toc = time.time()

    print("\nTotal time taken", toc - tic, "seconds.")
