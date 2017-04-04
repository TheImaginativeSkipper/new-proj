#Ryan Jarvis
#3/23/17
#heros invintory

inv=("steel sword",
     "chain mail armor",
     "light metal sheild",
     "strange yellow potion")

print("your inventory")

for item in inv:
    print(item)

input("press the enter key to continue")

#------------------------------------------------

print("you have",len(inv),"items in your possession.\n")

input("press enter to continue")

#-------------------------------------------------

index=int(input("enter an index number (0-3) for an item in your inventory:\n"))

print("at index", index,"is",inv[index])

#-------------------------------------------------

start=int(input("enter the index number to begin a slice:\n"))
          
finish=int(input("enter the index number to end the slice:\n"))
          
print("inventory[",start,"!",finish,"]is",end="")

print(inv[start:finish])

input("press enter to continue")

#-------------------------------------------------

chest=("gold","glowing red gem")
print("You find a damaged wooden chest. You open it to find:\n")

print(chest)
print("you add the items to your inventory")
inv+=chest
print("you inventory is now")
print(inv)

input("press enter to exit")













