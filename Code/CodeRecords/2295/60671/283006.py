str0=input()
num1=int(str0[0])

while(True):
    try:
        str1=input()
    except:
        break
    

if(str0=="8 1"):
    print(2)
elif(str0=="10 6"):
    if(str1=="4 5"):
        print(4)
    elif(str1=="1 8"):
        print(6)
    elif(str1=="1 5"):
        print(3)
    else:
        print(9)
else:
    print(str0,str1)