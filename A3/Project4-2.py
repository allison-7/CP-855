def main():
    print("Hike Calculator\n")
    miles = float(input("How many miles did you walk?: "))
    feet = milesToFeet(miles)
    print("You walked " + str(feet) + " feet.")

def milesToFeet(miles):
    return int(miles * 5280)

main()