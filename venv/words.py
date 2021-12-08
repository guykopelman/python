def word_count(path):
    """

    :param path: gt a path
    :return: how many words are in the file
    """
    counter = 0
    with open(path, "rb") as file:
        data = file.read()
        list_of_data = data.split()
    return len(list_of_data)


def appear_words(path):
    """

    :param path: get a path
    :return: how many time every word apper (return dict of words and the count)
    """
    counter = 0
    dict = {}
    with open(path, "rb") as file:
        data = file.read()
        data.decode('utf-8')
        list_of_data = data.split()
        for word in list_of_data:
            if word not in dict.keys():
                occurrences = data.count(word)
                dict[word] = occurrences
        return dict


def dict_print(dict):
    """

    :param dict:
    PRINT THE DICT
    """
    for key, value in dict.items():
        print(key, value , " ")


def main():
    print(word_count("stam_txt"))
    print(appear_words("stam_txt"))
    dict = {
        "first name": "guy",
        "last name": "kopelman",
        "year": 2003
    }

    dict_print(dict)


if __name__ == '__main__':
    main()
