import time


class AllFactors:
    """
    This class is a python implementation of the problem discussed in this
    video by mycodeschool - https://www.youtube.com/watch?v=dolcMgiJ7I0

    :Authors: pranaychandekar
    """

    @staticmethod
    def get_all_factors(number: int):
        """
        This method generates all the factors of a given non-negative number.

        :param number: The number corresponding to which we need all the prime factors
        :type number: int
        :return: All the factors
        :rtype: list
        """
        factors_a = []
        factors_b = []

        upper_limit = int(number ** 0.5) + 1

        for i in range(1, upper_limit, 1):
            if number % i == 0:
                factors_a.append(i)
                if i != int(number / i):
                    factors_b = [int(number / i)] + factors_b

        return factors_a + factors_b


if __name__ == "__main__":
    tic = time.time()

    number = 38808  # Enter a positive number here

    factors = AllFactors.get_all_factors(number)

    print("\nAll factors of", number, "are:", factors)

    toc = time.time()

    print("\nTotal time taken", toc - tic, "seconds.")
