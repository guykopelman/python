import math


def gcd(num1: int, num2: int):
    """
        The function gets 2 numbers and return their greatest common divide.
        :param num1: first number.
        :param num2: second number.
        :return: return the greatest common divide.
        """
    i = min(num1, num2)
    while i > 0:
        if num1 % i == 0 and num2 % i == 0:
            return i
        i -= 1
    return i


def main():
    num1 = int(input("enter a number"))
    num2 = int(input("enter a number"))
    n = gcd(num1, num2)
    print(n)


if __name__ == '__main__':
    main()
