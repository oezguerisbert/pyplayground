def en_filter(text):
    return "e" in text or "n" in text

def task5(_list):
    result = []
    for member in _list:
        if en_filter(member):
            result.append(member)

if __name__ == "__main__":
    _list = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]
    task5(_list)
