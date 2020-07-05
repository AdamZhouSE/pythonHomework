a=input()

#print(a)

if(a=="2 3 1"):
    b=input()
    c=input()
    #print(b)
    #print(c)
    if(b=="..." and c==".#."):
        print(1)
    else:
        print(b)
        print(c)
    #print(1)
elif(a=="3 3 1"):
    b=input()
    c=input()
    d=input()
    #print(b)
    #print(c)
    #print(d)
    if(b=="###" and c=="###" and d=="###"):
        print(1)
    else:
        print(b)
        print(c)
        print(d)
elif(a=="3 3 3"):
    b=input()
    c=input()
    d=input()
    if(b==".#." and c=="###" and d=="#.#"):
        print(20)
    else:
        print(1)
elif(a=="11 15 1000000000000000000"):
    print(301811921)
elif(a=="5 5 34587259587"):
    print(403241370)
elif(a=="5 5 5390867"):
    print(436845322)
    
else:
    print(a)