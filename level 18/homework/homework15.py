# 15)

def rame(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'divisible by both 3 and 5'
    elif num % 3 == 0:
        return 'divisible by 3'
    elif num % 5 == 0:
        return 'divisible by 5'
    else:
        return 'your num is not divisible by 3 or 5'

num = int(input("Enter a num: "))
print(rame(num))