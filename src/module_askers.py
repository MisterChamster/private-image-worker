from os.path import exists



def ask_path():
    while True:
        dir_path = str(input("Enter path: \n>> "))
        if exists(dir_path):
            return dir_path
