import math

def is_prime(num: int):
    """
    the function cheak if number is prime
    :param num: number from main
    :return: true if prime false Other
    """
    prime = True
    if num % 2 != 0:
        for i in range(3, int(math.sqrt(num))+1, 2):
            if num % i == 0:
                prime = False
                break
        return prime
    return False
    return prime

def main():
    list_of_prime = [i for i in range(1, 1000) if is_prime(i)]
    print(list_of_prime)


if __name__ == '__main__':
    main()
