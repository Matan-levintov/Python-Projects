from typing import Dict


def combine_coins(coin: str, numbers: list) -> str:  # great success
    return ", ".join([coin + str(number) for number in numbers])


# print(combine_coins('$', range(5)))

def intersection(list_1, list_2):
    # return list(set(filter(lambda x: x in list_2, list_1)))
    return list(set([x for x in list_1 if x in list_2]))

# print(intersection([1, 2, 3, 4], [8, 3, 9]))
# print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))


def is_prime(number):
    # comapres the returned list to an empty list to check if a number is a prime or not
    return [div for div in range(2, number) if number % div == 0] == []


# print(is_prime(42))
# print(is_prime(43))

def is_funny(string):
    # puts items into list of char is not a or h, if list is empty it means we have met the condions and the string is funny
    return [char for char in string if char not in ('a', 'h')] == []


# print(is_funny("hahahahahaha"))

def crack_password(password):
    # password = list(password)
    # for index, char in enumerate(password):
    #     password[index] = chr(ord(char)+2)
    # return "".join(password)
    return ''.join([chr(((ord(s) + 2) - ord('a')) % 26 + ord('a')) if s >= 'a' and s <= 'z' else s for s in password])


password = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(crack_password(password))
url = 'map'
print(crack_password(url))
