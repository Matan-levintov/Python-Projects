from functools import reduce
from os import truncate


def longest_word():
    with open('names.txt', 'r') as f:
        # prints the longest word in the file
        print(max(f.readlines(), key=len))


def sum_len():
    with open('names.txt', 'r') as f:
        # print the len of the all the words combined without the new line
        print(len(f.read().replace('\n', "")))


def shortest_names():
    with open('names.txt', 'r') as f:
        list_words = sorted([word for word in f.read().split(  # gets the whole file as a string then coverts it to a list of words with no \n characters and then returns the sorted list by len ascending
            '\n')], key=len)
        shortestNames = len(list_words[0])
        print(
            "\n".join([word for word in list_words if len(word) == shortestNames]))


def len_of_words_toNewFile():
    with open('names.txt', 'r') as f:
        with open('name_length.txt', 'w') as f2:
            f2.write('\n'.join([str(len(word))
                     for word in f.read().split('\n')]))


def prints_theLen_ofWords():
    """this function prints out the the words that have the length of the number that the user gave"""
    number = int(input("enter name length: ")
                 )  # remember the input always returns a str, if need number convert to int
    with open('names.txt', 'r') as f:
        print(
            '\n'.join([word for word in f.read().split('\n') if len(word) == number]))


# sum_len()
# shortest_names()
# len_of_words_toNewFile()
# prints_theLen_ofWords()
