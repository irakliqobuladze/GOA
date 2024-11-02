keyboard = {
    "keycaps color" : ["white", "gray"],
    "color" : "black",
    "light color" : "blue",
    "lights on" : True,
    "port" : "cable"
}

# 1 - გზა:
for i in keyboard.values():
    print(i)

# 2 - გზა:
for a,b in keyboard.items():
    print(b)    

# 3 - გზა:
for key,value in keyboard.items():
    print(value)    