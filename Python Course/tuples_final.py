

def sort_anagrams(list_of_strings):
    Returned_List = []  # The returned list
    words_already_used = []
    for word in list_of_strings:
        # list_of_strings.remove(word)
        current_list_of_words = [word]
        words_already_used += [word]
        # add_word = False
        # word = list(word)
        # if index != len(list_of_strings) - 1:
        for current_checked_word in list_of_strings:
            # try:
            #     current_checked_word = (list_of_strings[i])
            # except:
            #     break
            if sorted(current_checked_word) == sorted(word):
                if current_checked_word not in words_already_used:
                    # add_word = True
                    # if add_word:
                    current_list_of_words.append((current_checked_word))
                    words_already_used += [current_checked_word]
                    # add_word = False
                    # try:
                    # removes the word from the list
                    # list_of_strings.remove(current_checked_word)
                    # except:
                    #     pass
        Returned_List.append(current_list_of_words)
    return Returned_List


def main():
    list_of_words = list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating',
                                     'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))
    print(sort_anagrams(list_of_words) == [['deltas', 'desalt', 'slated', 'salted', 'staled', 'lasted'], [
        'retainers', 'ternaries'], ['pants'], ['generating', 'greatening'], ['smelters', 'termless', 'resmelts']])


if __name__ == '__main__':
    main()


# [['deltas', 'desalt', 'slated', 'salted', 'lasted'], ['retainers', 'retainers', 'ternaries'],
#     ['generating', 'generating', 'greatening'], ['termless', 'smelters', 'resmelts']]
# [['deltas', 'desalt', 'slated', 'salted', 'staled', 'lasted'], ['retainers', 'ternaries'],
#     ['pants'], ['generating', 'greatening'], ['smelters', 'termless', 'resmelts']]

# ---------------------------------------
# ['deltas', 'desalt', 'slated', 'salted', 'lasted'], ['retainers', 'retainers', 'ternaries'], ['generating', 'generating', 'greatening'], ['termless', 'smelters', 'resmelts']]
# [['deltas', 'desalt', 'slated', 'salted', 'staled', 'lasted'], ['retainers', 'ternaries'],
    # ['pants'], ['generating', 'greatening'], ['smelters', 'termless', 'resmelts']]
