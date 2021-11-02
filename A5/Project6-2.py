def main():
    print("The Wizard Inventory Program\n")
    displayMenu()
    wizardList = ["wooden staff", "wizard hat", "cloth shoes"]
    while True:        
        command = input("Command: ")
        if command.lower() == "show":
            show(wizardList)   
        elif command.lower() == "grab":
            grab(wizardList)
        elif command.lower() == "edit":
            edit(wizardList)
        elif command.lower() == "drop":
            drop(wizardList)  
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


def displayMenu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")

def show(wizardList):
    i = 1
    for item in wizardList:
        print(str(i) + ". " + item)
        i += 1
    print()

def grab(wizardList):
    if(len(wizardList) >= 4):
        print("You can't carry anymore items. Drop something first")
    else:
        item = input("Name: ")
        wizardList.append(item)
        print(item + " was added\n")

def edit(wizardList):
    n = int(input("Number: "))
    if n < 1 or n > len(wizardList):
        print("Invalid item number")
    else:
        item = input("Updated name: ")
        wizardList[n] = item
        print("Item number " + str(n) + " was updated")

def drop(wizardList):
    n = int(input("Number: "))
    if n < 1 or n > len(wizardList):
        print("Invalid item number")
    else:
        item = wizardList.pop(n-1)
        print(item + " was dropped")

if __name__=="__main__":
    main()
