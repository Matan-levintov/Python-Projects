import file1


class BirthDayCard(file1.GreetingCard):
    def __init__(self, receipient='Dana Ev', sender='Eyal Ch', age=0) -> None:
        super().__init__(receipient, sender)
        self._age = age

    def greetingmsg(self):
        super().greetingmsg()
        print(f'my age is {self._age} years old ')
