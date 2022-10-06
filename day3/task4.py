def task4_a(list_99):
    result = []
    for num in list_99:
        if "9" in f"{num}":
            result.append(num * 2)
    return result

def task4_b(list_99):

    return task4_a(list_99)[-1]
if __name__ == "__main__":
    print(task4_a([9,19,29,39,49,59,69]))
    print(task4_b([9,19,29,39,49,59,69]))

