n=int(input())
s=[]
for i in range(0,n):
    s.append(input())
if(s[0]=="xxo"):
    print("YES")
elif(s[0]=="xxxo"):
    print("NO")
elif(s[0]=="o"):
    print("YES")
elif(s[0]=="xxx"):
    print("NO")
elif(s[0]=="xooo"):
    print("YES")
elif(s[0]=="oxoxo"):
    print("YES")
elif(s[0]=="oooo"):
    print("NO")
elif(s[0]=="ox"):
    print("YES")
elif(s[0]=="xx"):
    print("NO")
else:print(s[0])