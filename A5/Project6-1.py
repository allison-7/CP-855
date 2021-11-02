import math
from functools import reduce

def main():
    print("Prime Number Checker\n")
    choice ="y"
    while choice.lower() == "y":
        num = int(input("Please enter an integer between 1 and 5000: "))
        isPrime = checkPrime(num)
        if(isPrime):
            print(str(num) + " is prime")
        else:
            factors = sorted(getPrime(num))
            strFactors = " ".join(str(i) for i in factors)
            print("It has " + str(len(factors)) + " factors: " + str(strFactors))
        choice = input("Try again (y/n)? ")
    
def checkPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def getPrime(n):
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
if __name__=="__main__":
    main()