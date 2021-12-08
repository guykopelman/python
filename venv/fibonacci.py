def recur_fibo(n):
    """
    the function return fibonaci in place n
    :param n: the place in series
    :return: the value of n place in fibo
    """
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


def main():
    # take input from the user
    nterms = int(input("How many terms? "))
    # check if the number of terms is valid
    if nterms <= 0:
        print("Plese enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(nterms):
            print(recur_fibo(i))


if __name__ == '__main__':
    main()
