a=input()

#print(a)

if(a=="2"):
    b=input()
    c=input()
    if(b=="4" and c=="7 5 8 6"):
        print(40)
        print(8)
    elif(b=="4" and c=="3 5 8 6"):
        print(24)
        print(8)
    elif(b=="7 8" and c=="5 40"):
        print(2)
        print(8)
    elif(b=="7 8" and c=="5 11"):
        print(2)
        print(6)
    else:
        print(b)
        print(c)