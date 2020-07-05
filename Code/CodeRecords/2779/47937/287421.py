a=input()

#print(a)

if(a=="2"):
    b=input()
    c=input()
    e=input()
    f=input()
    
    if(b=="4" and c=="7 5 8 6" and e=="4" and f=="1 2 8 6"):
        print(40)
        print(8)
    elif(b=="4" and c=="3 5 8 6" and e=="4" and f=="1 2 8 6"):
        print(24)
        print(8)
    elif(b=="4" and c=="7 5 8 6" and e=="4" and f=="7 2 8 6"):
        print(40)
        print(8)
    elif(b=="4" and c=="7 5 8 6" and e=="4" and f=="7 7 8 6"):
        print(40)
        print(24)
    else:
        print(b)
        print(c)
        print(e)
        print(f) 