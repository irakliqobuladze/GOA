def sum1(list1):
    res = 0

    for i in list1:
        try:
            res += i
        except:
            res += int(i)

    return res

print(sum1([1, 2, 3, 4, "5"]))   