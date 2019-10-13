import time


class PrimeOrNot:
    """
    This class is a python implementation of the problem discussed in this
    video by mycodeschool - https://www.youtube.com/watch?v=7VPA-HjjUmU

    :Authors: pranaychandekar
    """

    @staticmethod
    def is_prime(number: int):
        """
        This method tells whether a given non-negative number is prime or not.

        :param number: The number which needs to be verified.
        :type number: int
        :return: The result whether the given number is prime or not.
        :rtype: bool
        """
        result: bool = True
        if number < 2:
            result = False
        else:
            upper_limit = int(number ** 0.5) + 1
            for i in range(2, upper_limit, 1):
                if number % i == 0:
                    result = False
                    return result
        return result


if __name__ == "__main__":
    tic = time.time()

    number = 49  # Enter the number here

    if PrimeOrNot.is_prime(number):
        print("\nThe number", number, "is prime.")
    else:
        print("\nThe number", number, "is not prime.")

    toc = time.time()

    print("\nTotal time taken:", toc - tic, "seconds")
