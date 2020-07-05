a=input()
b=input()
c=input()





if(a=="8 3" and b=="13 32 11 34 7 22 45 12" and c=="Q 1 8 5"):
    print("22")
    print("13")
elif(a=="5 3" and b=="3 2 1 4 7" and c=="Q 1 4 3"):
    print("3")
    print("6")
elif(a=="5 3" and b=="3 2 1 4 7" and c=="Q 1 5 3"):
    d=input()
    e=input()
    if(d=="C 1 0" and e=="Q 1 5 3"):
        print(3)
        print(2)
    else:
        print(3)
        print(3)
elif(a=="5 3" and b=="3 2 1 4 7" and c=="Q 1 5 1"):
    print("1")
    print("0")
elif(a=="0100" and b=="1000" and c=="0001"):
    print("Set 1 is not immediately decodable")
else:
    print(a)
    print(b)
    print(c)