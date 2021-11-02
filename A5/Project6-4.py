def main():
    print("The Quarterly Sales Program")
    sales = getSales()
    t = total(sales)
    average = round(t / len(sales), 2)
    low = round(min(sales), 2)
    high = round(max(sales), 2)
    print("Total: "+ str(t))
    print("Average quarter: " + str(average))
    print("Lowest quarter: " + str(low))
    print("Higherst quarter: " + str(high))

def getSales():
    sales = [0,0,0,0]
    sales[0] = float(input("Enter sales for q1: "))
    sales[1] = float(input("Enter sales for q2: "))
    sales[2] = float(input("Enter sales for q3: "))
    sales[3] = float(input("Enter sales for q4: "))
    return tuple(sales)

def total(sales):
    t = 0
    for i in sales:
        t += i
    return round(t,2)

if __name__=="__main__":
    main()
