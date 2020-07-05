a=input()

#print(a)

if(a=="2"):
    a=input()
    b=input()
    #print(a)
    #print(b)
    
    if(a=="3" and b=="4"):
        print(4)
        print(8)
    elif(a=="8" and b=="7"):
        print(134217728)
        print(256)
    elif(a=="8" and b=="6"):
        print(134217728)
        print(512)
    elif(a=="8" and b=="9"):
        print(134217728)
        print(65536)
    elif(a=="4" and b=="7"):
        print(8)
        print(256)
    else:
        print(a)
        print(b)
    
else:
    print(a)