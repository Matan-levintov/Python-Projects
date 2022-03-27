class MusicNotes():
    def __init__(self):
        self._index = -1
        self.notes = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self.notes)-1:
            self.notes = list(map(lambda x: x*2, self.notes))
            self._index = -1
        if self.notes[self._index] == 98*2**5:
            raise StopIteration
        self._index = self._index + 1
        return self.notes[self._index]


notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)
