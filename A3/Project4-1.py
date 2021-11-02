def main():
    print("Even or Odd Checker\n")
    evenOdd = int(input("Enter an integer: "))
    result = checker(evenOdd)
    if(result):
        print("This is an even integer")
    else:
        print("This is an odd integer")

def checker(evenOdd):
    if((evenOdd % 2) == 0):
        return True
    else: 
        return False

main()
