import functools


def help_func(my_str):
    return my_str*2


def is_divideableBy4(number):
    return number % 4 == 0


def four_dividers(number):
    return (list(filter(is_divideableBy4, range(1, number+1))))


def double_letter(my_str):
    return list(map(help_func, my_str))


def add(n, n2):
    return int(n) + int(n2)


def sum_of_digits(number):
    return functools.reduce(add, list(str(number)))


print(sum_of_digits(104))


# print(four_dividers(9))
# print(four_dividers(3))


# print("".join(double_letter("python")))
# print("".join(double_letter("we are the champions!")))
