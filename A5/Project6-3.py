def main():
    print("Contact manager\n")
    displayMenu()
    contactList = [["Guido van Rossum", "gudio@guido.com", "559-023-7892"],["Eric Idle", "eric@ericidle.com", "+44  20 7946 0958"]]
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list(contactList)   
        elif command.lower() == "view":
            view(contactList)
        elif command.lower() == "add":
            add(contactList)
        elif command.lower() == "delete":
            delete(contactList)  
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

def displayMenu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("delete - delete a contact")
    print("exit - Exit program")

def list(contactList):
    if(len(contactList) == 0):
        print("There are no contacts")
        return
    else:
        i = 1
        for row in contactList:
            print(str(i) + ". " + row[0])
            i += 1

def view(contactList):
    n = int(input("Number: "))
    if n < 1 or n > len(contactList):
        print("Invalid item number")
    else:
        print("Name: "+ contactList[n-1][0])
        print("Email: " + contactList[n-1][1])
        print("Phone: " + contactList[n-1][2])

def add(contactList):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contactList.append(contact)
    print(contact[0] + " was added\n")

def delete(contactList):
    n = int(input("Number: "))
    if n < 1 or n > len(contactList):
        print("Invalid item number")
    else:
        contact = contactList.pop(n-1)
        print(contact[0] + " was deleted\n")

if __name__=="__main__":
    main()
