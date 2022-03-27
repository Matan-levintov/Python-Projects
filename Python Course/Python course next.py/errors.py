def read_file(file_name):
    print('__Content_Start__')
    try:
        f = open(file_name)
    except IOError:
        print('__No_Such_File__')
    else:
        print(f.readlines())
    finally:
        print('__Content_End__')


read_file('names.txt')
read_file('nofile.txt')
