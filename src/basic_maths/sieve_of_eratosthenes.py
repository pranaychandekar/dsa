import time


class SieveOfEratosthenes:
    """
    This class is a python implementation of the problem discussed in this
    video by mycodeschool - https://www.youtube.com/watch?v=eKp56OLhoQs

    :Authors: pranaychandekar
    """

    @staticmethod
    def generate_sieve(number: int):
        """
        This method generates the Sieve of Eratosthenes.

        :param number: The number for upto which we need to generate the Sieve of Eratosthenes.
        :type number: int
        :return: The list of booleans corresponding stating whether the index is prime or not.
        :rtype: list
        """
        sieve = [True] * (
            number + 1
        )  # Use boolean instead of number as bool takes less space in memory

        sieve[0] = sieve[1] = False  # 0 and 1 are neither prime nor composite

        upper_limit = int(number ** 0.5) + 1

        for i in range(2, upper_limit, 1):
            j = 2
            while i * j <= number:
                sieve[i * j] = False
                j += 1

        return sieve

    def get_all_primes(self, number: int):
        """
        This method generates prime numbers less than equal to the given number.

        :param number: The number for upto which we need all the prime numbers.
        :type number: int
        :return: The list of prime numbers less than equal to the given number.
        :rtype: list
        """
        primes = []

        sieve = self.generate_sieve(number)

        for i in range(len(sieve)):
            if sieve[i]:
                primes.append(i)

        return primes


if __name__ == "__main__":
    tic = time.time()

    number = 5  # Enter a non-negative integer here.

    solution = SieveOfEratosthenes()
    primes = solution.get_all_primes(number)

    print("\nAll primes less than equal to", number, ":", primes)

    toc = time.time()

    print("\nTotal time taken", toc - tic, "seconds.")
