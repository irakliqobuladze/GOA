# 2)

#tuple - იქმნება ჩვეულებრივი ფრჩხილებით,სადაც შეგვიძლია შევინახოთ ცვლადები.tuple'ში შეგვიძლია გამოვიყენოთ indexing და slicing.ასევე tuples-ს აქვს სხვა ფუნქციებიც მაგალითად: *rest

tuple = (10, 7, 9, 4, 3, 8)
tuple = sorted(tuple)[::-1]

print(tuple)

max_point, *rest = tuple
print(max_point) 
print(rest)

