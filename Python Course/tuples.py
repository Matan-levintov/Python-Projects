# data = ("self", "py", 1.543)
# format_string = f"Hello {data[0]}.{data[1]} learner, you have only {data[2]:.1f} unites left before you finish the course"
# print(format_string)


def mult_tuple(tuple1, tuple2):
    my_list = []
    for t1 in tuple1:
        for t2 in tuple2:
            pair = t1, t2
            revpair = t2, t1
            my_list.append(pair)
            my_list.append(revpair)
    return tuple(my_list)


def sort_2nd(elment):
    return elment[1]


def sort_prices(list_of_tuples):
    list_of_tuples.sort(key=sort_2nd, reverse=True)
    return list_of_tuples


def sort_anagrams(list_of_strings):
    returned_List = []  # this is the returned list
    # index = 0
    # keep_looping = True
    # while keep_looping:
    for words in list_of_strings:
        Add_Word = True
        # this the the list that builds the returned list
        words_string = []
        # words = str(words)
        word = list(words)  # make a list of the letters that are in words
        # print(word)
        # print(words)
        # for words in list_of_strings:
        for letter in words:  # loops through every letter in the current word and check if it has the same letters as the current word
            if letter not in word:  # if not it doesn't add the word the to the sub list
                Add_Word = False
        if Add_Word:
            words_string.append(words)
            list_of_strings.remove(words)
            # print(list_of_strings)
        returned_List.append(words_string)
        # if list_of_strings:
        #     words_string = []
        #     # index += 1
        # if not list_of_strings:  # empty list is a fasle boolean, so we use not to get a true statement and act apon it
        #     keep_looping = False
    return returned_List


def main():
    # products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    # print(sort_prices(products))
    # first_tuple = (1, 2)
    # second_tuple = (4, 5)
    # print(mult_tuple(first_tuple, second_tuple))
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating',
                     'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))


if __name__ == "__main__":
    main()
