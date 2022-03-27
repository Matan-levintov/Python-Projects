import winsound
notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }

# print(type(notes.split('-')))
# Yes this is iterable, but that's expected because from split we get a list
# print(dir(notes.split('-')))

noteAndDuration = []
# for note in notes.split('-')
# returns a list of lists of when the element is a list of the note and the duration
noteAndDuration = [note.split(',') for note in notes.split('-')]
# print(noteAndDuration)
for freq, duration in noteAndDuration:
    frequency = freqs[freq]
    winsound.Beep(frequency, duration)
