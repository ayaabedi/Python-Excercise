#each item with its value
items = {
    "Armor" : 3,
    "SuperTonic" : 2,
    "Shuriken" : 5,
    "Evade" : 2,
    "Sacrifice" : 2
    }
coins = 5
mylist = []

def listItems():
    number = 1
    print("")
    print("     Blacksmith Store")
    print("===========================")
    for key,value in items.items():
        print("{}. {} for {} coins".format(number, key, value))
        number+= 1
    print("")
    print(">>")


raw_input = int(input())
if (raw_input == 1 and coins >= items["Armor"]):
    mylist.append(items.keys())
elif (raw_input == 2):
    mylist.append(items["SuperTonic"])

print(mylist)