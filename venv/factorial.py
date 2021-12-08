def main():
    """
    This function get a number from user and calculate  the factorial of him

    """
    num = int(input("enter a num"))
    factorial = 1
    while num < 0:
        num = int(input("enter a num"))
    for i in range(1, num + 1):
        factorial *= i
    print("the factorial of", num, "is ", factorial)


if __name__ == '__main__':
    main()
