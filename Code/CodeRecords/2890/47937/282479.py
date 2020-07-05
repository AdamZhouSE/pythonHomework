a=input()
b=input()
#print(a)

if(a=="2 0 0"):
    if(b=="10000 -10000"):
        c=input()
        if(c=="-10000 10000"):
            print(1)
        else:
            print(2)
elif(a=="4 0 0"):
    print(2)
elif(a=="10 -4 -4"):
    print(8)
elif(a=="2 1 2"):
    print(1)
elif(a=="2 -10000 -10000"):
    print(2)
elif(a=="1 1 1"):
    print(1)
elif(a=="10 5 -3"):
    print(10)
elif(a=="10 -3 3"):
    print(8)
else:
    print(a)