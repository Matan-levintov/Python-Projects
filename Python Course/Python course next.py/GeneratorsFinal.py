def gen_secs():
    sec = 00
    while sec < 60:
        yield sec
        sec = (sec)+1


def gen_minutes():
    min = 0
    while min < 60:
        # if (min) == 60:
        # min = 0
        yield min
        min = ((min)+1)


def gen_hours():
    hour = 00
    while hour < 24:
        # if (hour) == 24:
        # hour = 00
        yield hour
        hour = ((hour)+1)


def gen_time():
    secs = (gen_secs())
    mins = (gen_minutes())
    hours = (gen_hours())
    while True:
        for hour in hours:
            for min in mins:
                for sec in secs:
                    yield (f"{hour}:{min}:{sec}")
                yield (f"{hour}:{min}:{sec}")


for gt in gen_time():
    print(gt)
