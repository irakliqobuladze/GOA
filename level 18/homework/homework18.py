# 18)

def number(num):
    result_lst = []
    for i in num:
        result_lst.append(i ** 2)
    return result_lst

num = [3,12,5,2,6]
print(number(num))