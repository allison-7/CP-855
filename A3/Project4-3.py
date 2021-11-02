def main():
    displayTitle()
    choice = "y"
    while choice.lower() == "y":
        conversion = getInput()
        if conversion == "a":
            feet = float(input("Enter feet: "))
            meters = round((feet * 0.3048),2)
            print(str(meters) + " meters")
        elif conversion == "b":
            meters = float(input("Enter meters: "))
            feet = round((meters / 0.3408), 2)
            print(str(feet) + " feet")
        choice = input("Continue (y/n): ")
    print("Thanks, bye!")

def displayTitle():
    print("Feet and Meters Calculator\n")

def getInput():
    print("Conversions Menu: ")
    print("a. Feet to Meters")
    print("b. Meters to Feet")
    choice = input("Select a conversion (a/b): ")
    return choice.lower()

if __name__=="__main__":
    main()