print("Pay Check Calculator\n")

hours = float(input("Hours worked\t"))
rate = float(input("Hourly Pay Rate\t"))

gross = round(hours * rate, 2)
print("Gross Pay:\t"+ str(gross))
tax_rate = 18
print("Tax Rate:\t" + str(tax_rate) + "%") 
tax_amount = round(gross * tax_rate/100,2)
print("Tax Amount:\t"+  str(tax_amount))
take_home = gross - tax_amount
print("Take Home Pay: \t" + str(take_home))
