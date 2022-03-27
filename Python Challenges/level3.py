import string
with open('level3raw.txt') as f:
    data = f.read().strip()
    list_of_chars = []
    for index, value in enumerate(data):
        try:
            if data[index] not in string.ascii_uppercase: # i figured it out , just forgot an edge case where the first letter is not a cap
                if data[index+1] in string.ascii_uppercase:
                    if data[index+2] in string.ascii_uppercase:
                        if data[index+3] in string.ascii_uppercase:
                            if data[index+4] in string.ascii_lowercase:
                                if data[index+5] in string.ascii_uppercase:
                                    if data[index+6] in string.ascii_uppercase:
                                        if data[index+7] in string.ascii_uppercase:
                                            if data[index+8] not in string.ascii_uppercase:
                                                list_of_chars += data[index+4]

        except:
            pass
print("".join(list_of_chars))
