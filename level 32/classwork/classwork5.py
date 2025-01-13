# MAPS:

# 1. 

list1 = [1, 2, 3, 4, 5]
map_list1 = list(map(lambda x: x ** 2, list1))
print(map_list1)

# 2. 

list2 = [0, 20, 30, 40]
map_list2 = list(map(lambda x: x * 33.8, list2))
print(map_list2)

# 3.

list3 = ["hello", "world", "python"]
map_list3 = list(map(lambda s: s.capitalize(), list3))
print(map_list3)

# FILTERS:

# 1. 

list4 = [1, 2, 3, 4, 5, 6, 7, 8]
map_list4 = list(filter(lambda x: x % 2 == 0, list4))
print(map_list4)

# 2.

list5 = ["cat", "house", "tree", "car"]
map_list5 = list(filter(lambda s: len(s) > 4, list5))
print(map_list5)

# 3.

list6 = [3, 9, 15, 22, 27, 30]
map_list6 = list(filter(lambda x: x % 3 == 0, list6))
print(map_list6)