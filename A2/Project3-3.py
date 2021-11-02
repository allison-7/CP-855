print("Change Calculator\n")

more = "y"

while more.lower() == "y": 
    cents = int(input("Enter number of cents (0-99): "))

    quarters = int(cents/25)
    remain = cents - (quarters*25)
    dimes = int(remain/10)
    remain = remain - (dimes*10)
    nickels = int(remain/5)
    remain = remain - (nickels*5)

    print("Quaters: " + str(quarters))
    print("Dimes: " + str(dimes))
    print("Nickels: " + str(nickels))
    print("Pennies: " + str(remain))
    
    more = input("\nContinue? (y/n): ")
print("Bye!")