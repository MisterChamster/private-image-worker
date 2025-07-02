from os.path import exists

def ask_path():
    while True:
        dir_path = str(input("Enter path: \n>> "))
        if exists(dir_path):
            return dir_path

def ask_mainloop_action():
    while True:
        action = str(input("Enter action: \nexit - Exit program.\n\n>> "))

        if action not in ["exit"]:
            print("Incorrect input!!")

        else:
            return action
