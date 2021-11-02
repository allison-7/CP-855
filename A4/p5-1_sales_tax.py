#!/usr/bin/env python3

def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    total_after_tax = round(total + sales_tax(total), 2)
    print("Total after tax: ", total_after_tax)

def sales_tax(total):
    sales_tax = total * 0.06
    return sales_tax

if __name__=="__main__":
    main()

