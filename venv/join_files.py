def join_file(path1, path2, path3):
    """

    :param path: gt a path
    :return: how many words are in the file
    """

    with open(path1, "rb") as file:
        data = file.read()
    with open(path2, "rb") as file:
        data += file.read()
    with open(path3, "wb") as file:
        file.write(data)


def main():
    join_file(r"C:\Users\HP\PycharmProjects\untitled5\venv\file_to_join.txt", r"C:\Users\HP\PycharmProjects\untitled5\venv\second_file.txt", r"C:\Users\HP\PycharmProjects\untitled5\venv\write_file.txt")


if __name__ == '__main__':
    main()
