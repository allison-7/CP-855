def main():
    displayTitle()
    choice = "y"
    while choice.lower() == "y":
        itemTotal = getItems()
        print("Total: " + str(itemTotal))
        tax = getTax(itemTotal)
        print("Sales Tax: " + str(tax))
        grandTotal = getTotal(itemTotal, tax)
        print("Total after tax: " + str(grandTotal))
        choice = input("Continue (y/n)? ")
    print("Bye")

def displayTitle():
    print("Sales Tax Calulator")

def getItems():
    print("ENTER iTEMS (ENTER 0 TO END)")
    item = float(input("Cost of item: "))
    while item != 0:
        itemTest = float(input("Cost of item: ")) 
        if(itemTest == 0):
            return item
        else:
            item += itemTest

def getTax(itemTotal):
    return round((itemTotal * 0.06),2)

def getTotal(itemTotal, tax):
    return itemTotal + tax

if __name__=="__main__":
    main()