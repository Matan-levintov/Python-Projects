def my_mp3_playlist(file_path):
    my_dict = dict()
    with open(file_path, 'r') as file:
        file_content = []
        count = {}  # the number of times that an acotr has pefromed
        for row in file:
            row.rstrip()
            row = row.replace(':', "")
            file_content.append(row.split(';'))
        for item in file_content:
            my_dict[int(item[2])] = item[0]
            if item[1] in count:
                count[item[1]] += 1
            else:
                count[item[1]] = 1
        longest_song = my_dict[max(my_dict.keys())]
        number_of_songs = len(my_dict)
        # search for the max vaulue, by using a key that retunes that value for every key instead of the key itself
        who = max(count, key=count.get)
    return longest_song, number_of_songs, who


def my_mp4_playlist(file_path, new_song):
    file = []
    with open(file_path, 'r+') as f:
        for row in f:
            new_row = row.split(';')
            # new_row.pop()
            file.append(new_row)
            # new_row.remove('\n')
            # file.append(row.split(';'))
        while len(file) < 3:
            file.append('\n')
        file[2][0] = new_song
        # something = "".join(str(v) for v in file)
        just_alist = []
        count = 0
        for row in file:
            # if count != 0:
            # just_alist += ";"
            # count += 1
            for item in row:
                # if item == '\n':
                just_alist.append(item+";")
        output = "".join(just_alist)
        print(output)
        # f.write(output)

        # print(my_mp3_playlist('songs.txt'))
my_mp4_playlist('songs.txt', "python love story")
