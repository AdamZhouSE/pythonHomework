s=input()
re=[]
l=[]
for i in range(0,len(s)):
    if s[i]=="(":
        temp=len(l)
        l.append(temp)
        re.append(temp)
    elif s[i]==")":
        re.append(l[-1])
        del l[-1]
max_depth=max(re)
flag=int(max_depth/2)
for i in range(0,len(re)):
    if re[i]<=flag:
        re[i]=0
    else:
        re[i]=1
print(re)