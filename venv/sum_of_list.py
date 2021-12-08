def sum_of_list():
    """
    the function print the list and the sum of the list values          
    """
    size = int(input("enter the size of the list"))
    numberList = []
    sum = 0
    for i in range(size):
        numberList.append(int(input("enter a number\n")))
        sum+=numberList[i]
    print("the list: ",numberList)
    print("\nsum: ", sum)








def main():
    sum_of_list()




if __name__ == '__main__':
    main()