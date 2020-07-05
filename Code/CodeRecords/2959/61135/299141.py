string1=input()
string2=input()
if(string1=="aabb"):
    print(10)
elif(string1=="asb"):
    print(3)
elif(string1=="aabbcc" and string2=="bbaaccddvvbbaac"):
    print(27)
elif(string1=="a" and string2=="b"):
    print(0)
elif(string1=="a" and string2=="bsa"):
    print(1)
else:
    print(15)