cp = float(input("Enter Cost Price (CP): "))
sp = float(input("Enter Selling Price (SP): "))


if sp > cp:
    profit = sp - cp
    print("You made a Profit of:", profit)
elif cp > sp:
    loss = cp - sp
    print("You incurred a Loss of:", loss)
else:
    print("No Profit, No Loss!")
