x= int(input("enter your number"))
y= int(input("enter your number"))
z= int(input("enter your number"))

if x>y:
    if x>z:
        print(f"{x}is greatest number")
    elif x<z:
        print(f"{z}is greatest number")
              
elif y>x:
    if y>z:
        print(f"{y}is greatest number")
    elif y<z:
        print(f"{z}is greatest number")
else:
    print(f"{z}is greatest number")             
              