print("Travel Time Calculator\n")

miles = int(input("Enter miles: "))
mph = int(input("Enter miles per hour: "))
print("")
print("Estimated travel time")
#hours = miles/mph 
#minutes = miles%mph
print("Hours " + str(int(miles/mph)))
print("Minutes " + str(int(miles%mph)))