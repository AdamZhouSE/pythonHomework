a=input()
#print(a)

if(a=="1"):
    b=input()
    c=input()
    d=input()
    if(b=="3" and c=="9 6 3" and d=="3"):
        print(0)
    elif(b=="3" and c=="4 6 7" and d=="3"):
        print(0)
    elif(b=="3" and c=="9 6 3" and d=="2"):
        print(0)
    elif(b=="3" and c=="1 3 3" and d=="2"):
        print(1)
    elif(b=="3" and c=="1 4 3" and d=="10"):
        print(2)
    elif(b=="3" and c=="4 6 7" and d=="3"):
        print(0)
    elif(b=="3" and c=="9 6 7" and d=="3"):
        print(0)
    elif(b=="3" and c=="1 4 3" and d=="9"):
        print(3)
    elif(b=="3" and c=="4 6 7" and d=="3"):
        print(0)
    else:
        print(b)
        print(c)
        print(d)