import time


class BinaryConverter:
    """
    This class is a python implementation of the problem discussed in this
    video by mycodeschool - https://www.youtube.com/watch?v=4vNlt_EDw1Q

    :Authors: pranaychandekar
    """

    @staticmethod
    def decimal_to_binary(decimal: int):
        """
        This method converts a non-negative decimal number to its equivalent binary representation.

        :param decimal: The non-negative decimal number.
        :type decimal: int
        :return: The binary representation.
        :rtype: str
        """
        binary = ""

        if decimal == 0:
            return decimal

        while decimal != 0:
            binary = str(decimal % 2) + binary
            decimal = decimal // 2

        return binary

    @staticmethod
    def binary_to_decimal(binary: str):
        """
        This method converts a binary number to its equivalent decimal representation.

        :param binary: The binary representation.
        :type binary: str
        :return: The decimal value of the passed binary string.
        :rtype: int
        """
        decimal = 0

        for element in binary:
            decimal = 2 * decimal + int(element)

        return decimal


if __name__ == "__main__":
    tic = time.time()

    decimal = 5  # Enter a non-negative number to convert to binary representation

    solution = BinaryConverter()
    binary = solution.decimal_to_binary(decimal)

    print("\nBinary representation of decimal", decimal, "is", binary)

    toc = time.time()

    print("\nTotal time taken", toc - tic, "seconds.")

    tic = time.time()

    binary = (
        "10101"
    )  # Enter a binary string to be converted to a decimal representation

    decimal = solution.binary_to_decimal(binary)

    print("\nDecimal value of binary string", binary, "is", decimal)

    toc = time.time()

    print("\nTotal time taken", toc - tic, "seconds.")
