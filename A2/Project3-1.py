print("Letter Grader Converter\n")

more = "y"

while more.lower() == "y":
    grade = int(input("Enter numerical grade: "))
    if grade >= 88:
        print("Letter grade: A")
    elif grade >= 80 and grade <=87:
        print("Leter grade : B")
    elif grade >= 67 and grade <= 79:
        print("Letter grade: C")
    elif grade >= 60 and grade <= 66:
        print("Letter grade: D")
    else:
        print("Leter grade: F")
    more = input("Continue? (y/n): ")

print("Bye!")