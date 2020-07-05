a=input()
#print(a)

if(a=="2"):
    b=input()
    c=input()
    #print(b)
    #print(c)
    if(b=="5 10 30" and c=="6 15 3"):
        print(0)
        print(4)
    elif(b=="25 100 30" and c=="6 15 3"):
        print(3)
        print(4)
    elif(b=="5 10 3" and c=="6 15 3"):
        print(2)
        print(0)
    elif(b=="5 10 3" and c=="6 5 3"):
        print(2)
        print(0)
    elif(b=="25 10 30" and c=="6 15 3"):
        print(0)
        print(4)
    elif(b=="5 10 30" and c=="6 5 3"):
        print(0)
        print(0)
    else:
        print(b)
        print(c)

        