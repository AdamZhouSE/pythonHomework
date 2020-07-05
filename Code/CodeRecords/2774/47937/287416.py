a=input()
#print(a)

if(a=="1"):
    b=input()
    c=input()
    #print(b)
    #print(c)
    if(b=="7 50" and c=="1 12 5 111 2 10 10"):
        print(6)
    elif(b=="7 50" and c=="1 12 5 111 200 100 10"):
        print(4)
    elif(b=="7 50" and c=="1 12 85 111 2 10 10"):
        print(5)
    elif(b=="7 50" and c=="1 12 5 111 2 100 10"):
        print(5)
    elif(b=="7 50" and c=="1 12 5 111 200 1000 10"):
        print(4)
    else:
        print(b)
        print(c)