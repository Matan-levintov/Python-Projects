class Dog:
    count_animals = 0

    def __init__(self, age, name='doggy'):
        self._name = name
        self._age = age
        Dog.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


def main():
    husky = Dog(2, 'husky')
    Sicho = Dog(2)
    husky.birthday()
    # print(husky.get_age())
    # print(Sicho.get_age())
    print(Sicho.get_name())
    print(husky.get_name())
    Sicho.set_name('Sicho')
    print(Sicho.get_name())
    print(husky.count_animals)
    print(Dog.count_animals)


if __name__ == '__main__':
    main()
