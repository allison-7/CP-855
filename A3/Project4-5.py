import random

def main():
    displayTitle()
    choice = "y"
    while choice.lower() == "y":
        die1 = rollDie()
        print("Die 1: "+ str(die1))
        die2 = rollDie()
        print("Die 2: "+ str(die2))
        total = die1 + die2
        checkDie(die1,die2)
        choice = input("Roll again? (y/n) ")
    print("Bye")

def displayTitle():
    print("Dice Roller")

def rollDie():
    return random.randint(1, 6)

def checkDie(die1, die2):
    if((die1 == 1) and (die2 == 1)):
        print("Snake eyes!")
    elif((die1 == 6) and die2 == 6):
        print("Boxcars!")

if __name__=="__main__":
    main()