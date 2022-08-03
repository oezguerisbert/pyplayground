def getDivisableBy5(mylist):
    result = []
    for num in mylist:
        if num % 5 == 0:
            result.append(num)
    return result

print(getDivisableBy5([0,1,5,15,25,323,150,450265]))
