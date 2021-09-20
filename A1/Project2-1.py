print("Registration Form\n")

name = str(input("First name:\t "))
lname = str(input("Last name:\t "))
birthYear = str(input("Birth year:\t "))

print("Welcome " + name + " " + lname)
print("Your registration is complete")
temp = name + "*" + birthYear  
print("Your temporary password is " + temp)                                                        