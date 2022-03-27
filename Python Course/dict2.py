def count_chars(my_str: str) -> dict:
    Dict = dict()
    for element in my_str:
        Dict[element] = my_str.count(element)

    return Dict


def inverse_dict(my_dict):
    new_dic = {}
    items = my_dict.items()
    for item in items:
        if item[1] in new_dic:
            new_dic[item[1]] = new_dic[item[1]] + [item[0]]
        else:
            new_dic.update({item[1]: [item[0]]})
    return new_dic


course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))

# )magic_str = "abra cadabra"
# print(count_chars(magic_str)
