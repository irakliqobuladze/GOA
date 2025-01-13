def manual_map(func,x):
    res = []

    for i in x:
        res.append(func(i))

    return res

print(manual_map(lambda x: x * 2, [1, 2, 3, 4, 5]))