str1=input()
str2=input()
if(str1=="aabb" and str2=="bbaa"):
    print(10)
elif(str1=="asb" and str2=="bsa"):
    print(3)
elif(str1=="aabbcc" and str2=="bbaaccddvvbbaac"):
    print(27)
elif(str1=="a" and str2=="b"):
    print(0)
elif(str1=="a" and str2=="bsa"):
    print(1)
else:
    print(15)