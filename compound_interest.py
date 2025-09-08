principal= float(input("enter the principal amount: "))
rate = float(input("enter the annual interest rate (in %): "))
time= float(input("enter the time in years: "))
n= float(input("enter the number of times interest applied per year: "))


amount = principal * (1 + rate/(100*n)**(n*time))
compound_interest = amount - principal
print(f"compound Interest: {compound_interest:.2f}")
print(f"total amount: {amount:.2f}")