class Animal:
    zoo_name = 'Hayaton'  # this is a var that is shared to every instance of the class, every instance has it, no matter what, and you can acsses it even without an instense

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungery(self):
        return self._hunger > 0

    def feed(self):
        self._hunger -= 1

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("there you go sir")


class Cat(Animal):
    def talk(self):
        print('meow')

    def chase_laser(self):
        print('Meeeeow')


class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count=6):
        Animal.__init__(self, name, hunger)
        _stink_count = stink_count

    def talk(self):
        print('tsssss')

    def stink(self):
        print('Dear Lord')


class Unicorn(Animal):
    def talk(self):
        print('Good day, darling')

    def sing(self):
        print("I'm not your toy!")


class Dragon(Animal):
    def __init__(self, name, hunger=0, color='green'):
        Animal.__init__(self, name, hunger)
        _color = color

    def talk(self):
        print('Raaaawr')

    def breath_fire(self):
        print('@!@!@!@!@!@')


def main():
    brownie_dog = Dog('Brownie', 10)
    doggo = Dog('Doggo', 80)
    zelda_cat = Cat('Zelda', 3)
    kitty = Cat('Kitty', 80)
    stinky_skunk = Skunk('Stinky', stink_count=6)
    stinky_jr = Skunk('Stinky JR', hunger=80)
    keith_unicorn = Unicorn('keith', 7)
    clair = Unicorn('Clair', 80)
    lizzy_dragon = Dragon('Lizzy', 1450, 'blue')
    mcfly = Dragon('McFly', 80)
    zoo_lst = [brownie_dog, zelda_cat,
               stinky_skunk, keith_unicorn, lizzy_dragon, doggo, kitty, stinky_jr, clair, mcfly]
    for animal in zoo_lst:
        print(animal.__class__.__name__, animal.get_name())
        while animal.is_hungery():
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()


if __name__ == '__main__':
    main()
    print(Animal.zoo_name)
