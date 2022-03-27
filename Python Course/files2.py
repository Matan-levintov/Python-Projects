def copy_file_content(source, destination):
    with open(source, 'r') as input_source:
        content = input_source.readline()
    with open(destination, 'w+') as output:
        output.write(content)
        print(output.readlines())


def who_is_missing(file_name):
    with open(file_name, 'r') as input_file:
        content = input_file.read()
        content = content.split(',')
        print(content)
        for i in range(1, len(content)+1):
            if str(i) not in content:
                with open('found.txt', 'w') as output:
                    output.write(str(i))
                return i


print(who_is_missing('fineMe.txt'))
# copy_file_content("copy.txt", "paste.txt")
