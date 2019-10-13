import time


class GCD:
    """
    This class is a python implementation of the problem discussed in this
    video by mycodeschool - https://www.youtube.com/watch?v=7HCd074v8g8

    :Authors: pranaychandekar
    """

    def get_gcd_recursive(self, a: int, b: int):
        """
        This method is the implementation of finding GCD of two numbers using recursion technique.

        :param a: The first number.
        :param b: The second number.
        :type a: int
        :type b: int
        :return: The GCD of two numbers.
        :rtype: int
        """
        if b == 0:
            return a
        return self.get_gcd_recursive(b, a % b)

    @staticmethod
    def get_gcd_iterative(a: int, b: int):
        """
        This method is the implementation of finding GCD of two numbers using Euclid's algorithm.

        :param a: The first number.
        :param b: The second number.
        :type a: int
        :type b: int
        :return: The GCD of two numbers.
        :rtype: int
        """
        while b != 0:
            a, b = b, a % b
        return a


if __name__ == "__main__":
    tic = time.time()

    a = 56  # Enter the first non-negative number
    b = 98  # Enter the second non-negative number

    solution = GCD()

    gcd_iterative = solution.get_gcd_iterative(a, b)

    gcd_recursive = solution.get_gcd_recursive(a, b)

    assert gcd_iterative == gcd_recursive

    print("\nGCD of", a, "and", b, "is", gcd_iterative)

    toc = time.time()

    print("\nTotal time taken", toc - tic, "seconds.")
