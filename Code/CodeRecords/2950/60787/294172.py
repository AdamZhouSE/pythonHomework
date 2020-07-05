s=input()
re=[]
l=[]
wrong=False
for i in range(0,len(s)):
    if s[i]=="2":
        temp=len(l)
        l.append(temp)
        re.append(temp)
    elif s[i]=="5":
        if len(l)==0:
            wrong=True
            break
        else:
            re.append(l[-1])
            del l[-1]
max_depth=max(re)
if len(l)==0 and not wrong:
    print(max_depth+1)
else:
    print(-1)