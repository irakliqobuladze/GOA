keyboard = {
    "keycaps color" : ["white", "gray"],
    "color" : "black",
    "light color" : "blue",
    "lights on" : True,
    "port" : "cable"
}

print(keyboard)

# 1 - გზა:
for i in keyboard.keys():
    print(i)
    
# 2 - გზა:    
for a,b in keyboard.items():
    print(a)    