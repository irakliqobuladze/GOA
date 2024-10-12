  # 5)

def manual_max(listn):
    max_num = listn[0]

    for i in listn:
        if max_num < i:
            max_num = i

    return max_num

print(manual_max([1,100,255,370,9,1531,0,-3,20,-10]))