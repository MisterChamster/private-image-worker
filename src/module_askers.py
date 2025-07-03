from os.path import exists



def ask_path():
    while True:
        dir_path = str(input("Enter path: \n>> "))
        if exists(dir_path):
            return dir_path


def ask_mainloop_action():
    while True:
        action = str(input("Enter action: \n" \
        "ls - List all images in folder.\n" \
        "cd - Change program working directory.\n" \
        "cnv - Convert...\n" \
        "exit - Exit program.\n\n>> "))

        if action not in ["ls", "cd", "cnv", "exit"]:
            print("Incorrect input.\n")
        else:
            return action


def ask_convert_action():
    while True:
        action = str(input("Enter convert action: \n" \
        "lsh - \n" \
        "hpn - \n" \
        "hpd - \n" \
        "lsp - \n" \
        "pjn - \n" \
        "pjd - \n" \
        "rt  - Return.\n\n>> "))

        if action not in ["lsh", "hpn", "hpd", "lsp", "pjn", "pjd", "rt"]:
            print("Incorrect input.\n")
        else:
            return action
