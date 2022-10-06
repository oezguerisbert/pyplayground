def task1(_list):
    for x in _list:

        if x % 2 == 0:
            print(x)

def task2(_list):
    result = []
    for x in _list:
        if x % 5 == 0:
            result.append(x)
    return len(result)

if __name__ == "__main__":
    task1([1,2,3,4,5,6])
    print(f"length: {task2([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])}", )
