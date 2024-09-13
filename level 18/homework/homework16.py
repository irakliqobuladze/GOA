# 16)

def average(num):
    total = sum(num)
    count = len(num)
    average = total / count
    return int(average)

num = [1,3,4,5,2]
print(average(num))