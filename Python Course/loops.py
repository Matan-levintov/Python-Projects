def squared_numbers(start, stop):
    rList = []
    while start <= stop:
        rList.append(start**2)
        start += 1
    print(rList)


def is_greater(my_list, n):
    return_list = []
    for element in my_list:
        if element > n:
            return_list += [element]
    return return_list


def numbers_letters_count(my_str):
    CountDigit = 0
    CountNonDigit = 0
    for elm in my_str:
        if elm.isdigit():
            CountDigit += 1
        else:
            CountNonDigit += 1
    return [CountDigit, CountNonDigit]


def sequence_del(my_str):
    my_str = list(my_str)
    print(my_str)
    try:
        # could be swapped for in range(len(my_str))
        for index, letter in enumerate(my_str):
            while my_str[index] == my_str[index+1]:
                my_str.pop(index+1)
    except:
        pass
    my_str = "".join(my_str)
    print(my_str)


def seven_boom(end_number):
    List = []
    for number in range((end_number+1)):
        if number % 7 == 0 or "7" in str(number):
            List += ['Boom']
        else:
            List += [number]
    return List


def arrow(my_char, max_length):
    for times in range(1, max_length+1):
        print(my_char*times)
    for times2 in range((max_length)-1, 0, -1):
        print(my_char*times2)


def main():
    # squared_numbers(4, 8)
    # squared_numbers(-3, 3)
    # result = is_greater([1, 30, 25, 60, 27, 28], 28)
    # print(result)
    # print(numbers_letters_count("Python 3.6.3"))
    # print(seven_boom(17))
    # sequence_del("ppyyyyythhhhhooonnnnn")
    # sequence_del("SSSSsssshhhh")
    # sequence_del("Heeyyy   yyouuuu!!!")
    arrow('*', 5)


if __name__ == "__main__":
    main()
