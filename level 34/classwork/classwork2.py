def manual_filter(func,x):
    res = []

    for i in x:
        if func(i):
            res.append(i)

    return res

print(manual_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))