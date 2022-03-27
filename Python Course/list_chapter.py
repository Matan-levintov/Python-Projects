def shift_left(pList):
    """this functions gets a List of 3 and moves every element 1 left"""
    temp = pList[0]
    pList[0] = pList[1]
    pList[1] = pList[2]
    pList[2] = temp
    return pList


def format_list(my_list):
    """this function returns a string which has every element that has a even index number and the last element"""
    new_list = my_list[0:len(my_list):2]
    return ", ".join(new_list) + f" and {my_list[-1]}"


def extend_list_x(list_x: list, list_y: list):
    for index, vaulue in enumerate(list_y):
        list_x.insert(index, vaulue)
    return list_x


def are_lists_equal(list1, list2):
    list1.sort()
    list2.sort()
    return list1 == list2


def longest(my_list):
    return max(my_list, key=len)


def main():
    # x = [4, 5, 6]
    # y = [1, 2, 3]
    # print(extend_list_x(x, y))
    # Desired output is [1,2,3,4,5,6]
    # list1 = [0.6, 1, 2, 3]
    # list2 = [3, 2, 0.6, 1]
    # list3 = [9, 0, 5, 10.5]
    # print(are_lists_equal(list1, list2))
    # print(are_lists_equal(list1, list3))
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list1))


if __name__ == "__main__":
    main()
