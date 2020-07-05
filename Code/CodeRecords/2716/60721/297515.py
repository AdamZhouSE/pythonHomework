s=input()
s1=input()
s1=s1[3:5]
s=input()
s=s[3:5]
if(s=="/ " ):
    if(s1!=" /"):
        print(3)
    else:print(2)
elif(s=="  "):
    print(1)
else:
    if(s[0:1]=="/"):
        print(4)
    else:print(5)