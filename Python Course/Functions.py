import math


def func(num1, num2):
    """the func returns sum of the numers sqaured"""
    return math.pow(num1*num2, 2)


def main():
    print(func(4, 4))
    help(func)


if __name__ == "__main__":
    main()
