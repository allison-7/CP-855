from os import PathLike


print("Tip Calculator\n")

cost = float(input("Cost of meal:\t"))
tip_percent = int(input("Tip Percent:\t"))
print("")
tip_amount = cost * (tip_percent /100)
print("Tip Amount:\t" + str(round(tip_amount,2)))
print("Total Amount:\t" + str(round(cost+tip_amount,2)))