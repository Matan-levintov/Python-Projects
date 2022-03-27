from re import L, match
from typing import ItemsView, List, Match


def action1():
    print(List)


def action2():
    print(len(List))


def action3():
    item = input("type an item you want ot search for ")
    print(item in List)


def action4():
    item = input("type an item you want to count ")
    print(List.count(item))


def action5():
    item = input("type an item you want to delete ")
    List.remove(item)  # pop works on the index
    print(f"the new list is {List}")


def action6():
    item = input("type an item you want to add ")
    List.append(item)


def action7():
    for item in List:
        if len(item) < 3 or not item.isalpha():
            print(item)
    else:
        print("all items are valid")


def action8():
    for item in List:
        if List.count(item) > 1:
            List.remove(item)
    print(f"the list is {List}")
    # List = list(dict.fromkeys(List))


def main():
    global List
    List = (input("type a string ").split(","))
    while True:
        choice = int(input("choose a number from 1-9 "))
        if choice == 1:
            action1()
        elif choice == 2:
            action2()
        elif choice == 3:
            action3()
        elif choice == 4:
            action4()
        elif choice == 5:
            action5()
        elif choice == 6:
            action6()
        elif choice == 7:
            action7()
        elif choice == 8:
            action8()
        elif choice == 9:
            break
        else:
            print("invalid number, try again")


if __name__ == '__main__':
    main()
