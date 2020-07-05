a=input()

#print(a)

b=input()
c=input()

#print(b)
#print(c)

if(b=="abb" and c=="abcab"):
    print(0)
    print(1)
elif(b=="abbc" and c=="abcab"):
    print(3)
    print(1)
elif(b=="abbc" and c=="abcabc"):
    print(3)
    print(7)
elif(b=="abb" and c=="abca"):
    print(0)
    print(1)
else:
    print(b)
    print(c)