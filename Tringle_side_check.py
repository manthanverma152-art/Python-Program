a = float(input("enter side 1 : "))
b = float(input("enter side 1 : "))
c = float(input("enter side 1 : "))

if a+b > c and a+c > b and c+b > a:
    print("all sides form a valid triangle ")
else:
    print("all sides do not form a valid triangle")