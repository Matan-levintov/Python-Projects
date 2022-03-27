def are_files_equal(file1, file2):
    with open(file1, 'r') as file10:
        file1_txt = file10.readlines()
    with open(file2, 'r') as file20:
        file2_txt = file20.readlines()
    return file1_txt == file2_txt


# print(are_files_equal(
#     '/Users/matanlevintov/Developer/Python Stuff/Python Course/file1.txt', '/Users/matanlevintov/Developer/Python Stuff/Python Course/files2.txt'))

file = input("please enter a file path ")
task = input("please enter a task ")
with open(file, 'r') as file1:
    file_contents = []
    for line in file1:
        line = line.rstrip()
        file_contents += [line]
    if task == 'sort':
        words = []
        for line in file_contents:
            words += line.split(" ")
        words.sort()
        words = list(dict.fromkeys(words))
        print(words)
    elif task == 'rev':
        for row in file_contents:
            print(row[::-1])
    elif task == 'last':
        n = int(input("enter a int number "))
        file_contents.reverse()
        print(file_contents[:n])
