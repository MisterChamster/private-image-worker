def ask_convert_action():
    returns_dict = {"lsh": "list_heic",
                    "lsp": "list_png",
                    "htp": "heic_to_png",
                    "htj": "heic_to_jpg",
                    "ptj": "png_to_jpg",
                    "rt":  "return"}

    while True:
        print("Choose convert action: \n" \
        "lsh  - List all .heic files in folder\n" \
        "lsp  - List all .png files in folder\n" \
        "htp  - .heic to .png...\n" \
        "htj  - .heic to .jpg...\n" \
        "ptj  - .png to .jpg...\n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> ", end="")
        action = input()

        if action == "exit":
            return None
        if action in returns_dict:
            return action
        else:
            print("Incorrect input.\n")


def ask_htp_action():
    returns_dict = {"lsh": "list_heic",
                    "hpn": "heic_to_png_no_del",
                    "hpd": "heic_to_png_del",
                    "rt":  "return"}

    while True:
        print("Choose heic to png action: \n" \
        "lsh  - List all .heic files in folder\n" \
        "hpn  - Convert .heic files to .png files (leave heic files)\n" \
        "hpd  - Convert .heic files to .png files (delete heic files)\n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> ", end="")
        action = input()

        if action == "exit":
            return None
        elif action in returns_dict:
            return action
        else:
            print("Incorrect input.\n")


def ask_htj_action():
    returns_dict = {"lsh": "list_heic",
                    "hjn": "heic_to_jpg_no_del",
                    "hjd": "heic_to_jpg_del",
                    "rt":  "return"}

    while True:
        print("Choose heic to jpg action: \n" \
        "lsh  - List all .heic files in folder\n" \
        "hjn  - Convert .heic files to .jpg files (leave heic files)\n" \
        "hjd  - Convert .heic files to .jpg files (delete heic files)\n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> ", end="")
        action = input()

        if action == "exit":
            return None
        elif action in returns_dict:
            return action
        else:
            print("Incorrect input.\n")


def ask_ptj_action():
    while True:
        print("Choose png to jpg action: \n" \
        "lsp  - List all .png files in folder\n" \
        "pjn  - Convert .png files to .jpg files (leave png files)\n" \
        "pjd  - Convert .png files to .jpg files (delete png files)\n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> ", end="")
        action = input()

        if action == "exit":
            return None
        if action not in ["lsp", "pjn", "pjd", "rt"]:
            print("Incorrect input.\n")
        else:
            return action
