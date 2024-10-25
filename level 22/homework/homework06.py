# 6)

def manual_replace(str1, pre, aft):
    res = ""

    for i in str1:
        if i == pre:
            res += aft
        else:
            res += i

    return res

print(manual_replace("hello", "e", "."))
