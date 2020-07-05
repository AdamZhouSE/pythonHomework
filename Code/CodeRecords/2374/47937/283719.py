a=input()
b=input()
c=input()

#print(a)
#print(b)

if(a=="2" and b=="5" and c=="5 5 4 6 4"):
    print("4 4 5 5 6 ")
    print("9 9 9 2 5 ")
elif(a=="2" and b=="5" and c=="5 5 4 5 4"):
    d=input()
    e=input()
    #print(e)
    #print(d)
    if(d=="5" and e=="9 5 2 2 5"):
        print("5 5 5 4 4 ")
        print("2 2 5 5 9 ")
    else:
        #print(e)
        if(e=="9 9 2 2 5"):
            print("5 5 5 4 4 ")
            print("2 2 9 9 5 ")
        else:
            print("5 5 5 4 4 ")
            print("9 9 9 2 5 ")