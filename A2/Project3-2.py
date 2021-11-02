print("Tip Calculator\n")

cost = float(input("Cost of meal: "))

print("\n15%")

tip = round((cost * 0.15), 2)
amount = cost + tip

print("Tip amount: " + str(tip))
print("Total amount: " + str(amount))

print("\n20%")

tip = round((cost * 0.2), 2)
amount = cost + tip

print("Tip amount: " + str(tip))
print("Total amount: " + str(amount))

print("\n25%")

tip = round((cost * 0.25), 2)
amount = cost + tip

print("Tip amount: " + str(tip))
print("Total amount: " + str(amount))
