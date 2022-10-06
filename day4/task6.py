def en_filter(text):
    return "e" in text or "n" in text

def analyse_list_elements(_list):
    for entry in _list:
        item_length = len(f"{entry}")
        print(f"{type(entry)} {entry} -> {item_length}")

if __name__ == "__main__":
    _list = ["starving", 4, True, -3.2]
    analyse_list_elements(_list)
