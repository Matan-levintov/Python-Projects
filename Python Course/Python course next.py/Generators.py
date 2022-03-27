from typing import Generator


def translate(sentence):
    returned_sentence = []
    words = {'esta': 'is', 'la': 'the', 'en': 'in',
             'gato': 'cat', 'casa': 'house', 'el': 'the'}
    gen_list = (words[word] for word in sentence.split(' '))
    for word in gen_list:
        returned_sentence.append(word)
    return " ".join(returned_sentence)


# print(translate("el gato esta en la casa"))

def is_prime(n):
    # Corner case
    if n <= 1:
        return False
   # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    generator = (number for number in range(n+1, n**10) if is_prime(number))
    # for number in generator:
    # if is_prime(number):
    return next(generator)


# print(first_prime_over(1000000))

def parse_ranges(ranges_string):
    # ['1-2', '4-4', '8-10']
    first_gen = (ran.split('-') for ran in ranges_string.split(','))
    # print(list(first_gen))
    # the the list consists of 2 elements, thus by assinging 2 elements you move those vaulues to those 2 and then you can convert it to int and set the range function
    gen2 = (num for start, stop in first_gen for num in range(
        int(start), int(stop)+1))
    return gen2


# print(list(parse_ranges("1-2,4-4,8-10")))
# print(list(parse_ranges("0-0,4-8,20-21,43-45")))

def get_fibo():
    number1 = 0
    number2 = 1
    while number2 < 200:
        yield number1
        yield number2
        number1 += number2  # 0 + 1 = 1
        number2 += number1


for number in get_fibo():
    print(number)

# LETS FUCKING GO I DID IT, WOOOOOO I DID IT, I ALWAYS KNEW I COULD DO IT, AND I FUCKING DID IT
