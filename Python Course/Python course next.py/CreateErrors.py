class Under_Aged(Exception):
    def __init__(self, age):
        self._age = age

    def __str__(self):
        return f"You are underaged thus you won't get an invite. You are currently {self._age} years old meaning you will be able to get an invite in {18-self._age} years"

    def get_args(self):
        return self._age


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise Under_Aged(age)
    except Under_Aged:
        print("Under_Aged exception caught")
    else:
        print('You should sent an invite to', name)


send_invitation('Matan', 20)
send_invitation('Nigga', 17)
