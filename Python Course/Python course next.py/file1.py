class GreetingCard():
    def __init__(self, receipient='Dana Ev', sender='Eyal Ch') -> None:
        self._recipient = receipient
        self._sender = sender

    def greetingmsg(self):
        print(f'Hi, {self._recipient} from {self._sender}')
