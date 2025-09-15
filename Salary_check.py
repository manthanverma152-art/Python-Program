exp = int (input("enter your experience in years : "))
salary = int (input("enter your salary : "))
if  exp == 0 : 
    print("salary : ",salary)
elif 0< exp <=1 :
    print("salary : ", salary+ (5*salary)/100)
elif 1< exp <=3 :
    print("salary : ", salary+ (10*salary)/100)
elif 3< exp <=10 :
    print("salary : ", salary+ (15*salary)/100)
elif  exp > 10 :
    print("salary : ", salary+ (25*salary)/100)