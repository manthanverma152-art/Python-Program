a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("Before swapping: a =", a, "b =", b)

a, b = b, a

print("After swapping: a =", a, "b =", b)


# or by sing bitwise operator 


a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("Before swapping: a =", a, "b =", b)


a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping: a =", a, "b =", b)
