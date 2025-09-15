uname="Manthan"
passcode=1234
count=1
while(count<=3):
    username = input("enter username : ")
    password = int(input("enter your passowrd : "))


    if(uname==username and passcode==password):
        print("access granted")
        break
    else:
        print("TRY AGAIN")
        count+=1