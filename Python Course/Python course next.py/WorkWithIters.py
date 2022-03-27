from itertools import combinations_with_replacement, combinations


def print_only_numbers_that_are_divided_by_3():
    numbers = iter(list(filter(lambda x: not x % 3, range(1, 101))))
    for i in numbers:
        print(i)


def OneHundred_dollar_problem():
    money = [1, 1, 1, 1, 1, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20]
    count = 0
    # the amount represents the amout of money we have from each type
    for number in range(1, 16):
        iter = set(combinations(money, number))
        for itm in iter:
            if sum(itm) == 100:
                print(itm)
                count = count + 1
    print(count)
    # print(set(combinations_with_replacement(money, 4)) ==
    #   tuple(combinations_with_replacement(money, 4)))


OneHundred_dollar_problem()

# money = [1, 1, 1, 1, 1, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20]
# print(set(combinations(money, 2)))
