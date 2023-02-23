import os.path as path
import os
FILE_PATH = path.abspath(__file__).replace('test.py', '')
PROJECT_PATH = FILE_PATH

filename = str(input('enter file name: '))
file_content = str(input('enter file content: '))

if filename or filename != "":

    if path.exists(PROJECT_PATH + filename + '.txt'):
        print(filename + ' is exist !')
        print('choose your opperation: ')
        print('enter 0 for exit')
        print('enter 1 for reWrite File')
        print('enter 2 for delete file')
        user_choose = int(input('your choose: '))
        if user_choose <= 2:
            if user_choose == 0:
                print('you exited')
                exit()
            elif user_choose == 1:
                file = open(PROJECT_PATH + filename + '.txt', 'w')
                file.write(file_content)
            elif user_choose == 2:
                os.remove(PROJECT_PATH + filename + '.txt')
                if path.abspath(PROJECT_PATH + filename):
                    print('file ' + filename + ' successfully deleted')
                    exit()
        else:
            exit('you choose nothing')

        if path.abspath(PROJECT_PATH + filename):
            print('file successfully maked')
        else:
            print('something went wrong plz try again later')
            exit()
    else:
        file = open(PROJECT_PATH + filename + '.txt', 'w')
        file.write(file_content)

        if path.abspath(PROJECT_PATH + filename):
            print('file successfully maked')
            exit()
        else:
            print('something went wrong plz try again later')
            exit()
else:
    print('you have to write a string for filename')
    exit()
