with open('level2raw.txt') as f:
    data = f.read()
    count = {}
    for c in data:
        count[c] = count.get(c, 0) + 1


print(count)
