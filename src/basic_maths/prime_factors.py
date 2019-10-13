import time


class PrimeFactors:
    """
    This class is a python implementation of the problem discussed in this
    video by mycodeschool - https://www.youtube.com/watch?v=6PDtgHhpCHo

    :Authors: pranaychandekar
    """

    @staticmethod
    def get_all_prime_factors(number: int):
        """
        This method finds all the prime factors along with their power for a given number.

        :param number: The non-negative number for which we want to find all the prime factors.
        :type number: int
        :return: All the prime factors with their corresponding powers.
        :rtype: dict
        """
        prime_factors = {}

        upper_limit = int(number ** 0.5) + 1

        for i in range(2, upper_limit, 1):
            if number % i == 0:
                count = 0
                while number % i == 0:
                    number /= i
                    count += 1
                prime_factors[i] = count

        if number != 1:
            prime_factors[int(number)] = 1

        return prime_factors


if __name__ == "__main__":
    tic = time.time()

    number = 99

    prime_factors = PrimeFactors.get_all_prime_factors(number)

    print("\nThe prime factors of number", number, "are:", prime_factors)

    toc = time.time()

    print("\nTotal time taken", toc - tic, "seconds.")
