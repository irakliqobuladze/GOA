str1 = "hElLo WoRld"

print(str1.lower()) # თუ ასოები დიდია, აპატარავებს
print(str1.upper()) # თუ ასოები პატარაა, ადიდებს
print(str1.capitalize()) # ადიდებს წინადადების 1-ლ ასოს
str1 = str1.swapcase() #დიდ ასოებს აპატარავებს, პატარებს კი ადიდებს
print(str1)

print("hello world".find("l")) # გვიჩვენებს ჩვენ მიერ არჩეული ასოს ინდექს

car = "toyota"
print(len(car)) # გვიჩვენებს სიტყვის/წინადადების სიგრძეს ციფრებით

colors = ["Red", "Blue", "Yellow"]
colors.append("black") # ამატებს ახალ ელემენტს სიის ბოლოში
colors.insert(1,"brown") # ამატებს ელემენტს სადაც გვსურს(რომელ ინდექსს დავწერთ)
colors.pop(2) # შლის სიიდან ელემენტს რომელიც ჩვენ გვსურს
colors.remove("Red") # იგივეა როგორც pop.
print(colors)


