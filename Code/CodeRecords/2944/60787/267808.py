left=0
s=list(input())
flag=True
for i in range(0,len(s)):
    if s[i]=="(":
        left+=1
    elif s[i]==")":
        if left==0:
            flag=False
            break
        else:
            left-=1
if flag and left==0:
    print("YES")
else:
    print("NO",end="")