class BigThing:
    def __init__(self, something=None):
        self._something = something

    def size(self):
        if isinstance(self._something, int) or isinstance(self._something, float):
            return self._something
        else:
            return len(self._something)


class BigCat(BigThing):
    def __init__(self, weight=0):
        super().__init__(self)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            print('very fat')
        elif self._weight > 15:
            print('fat')
        else:
            print('ok')


def main():
    cute = BigCat(22)
    cute.size()
    mything = BigThing('balloon')
    print(mything.size())


if __name__ == '__main__':
    main()
