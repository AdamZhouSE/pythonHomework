begword=input()
edword=input()
a=eval(input())
q=[begword]
m={begword:1}
flag=False
ans=0
while(len(q)!=0):
    wd=q[0]
    del q[0]
    for i in range(len(wd)):
        newwd=wd
        for ch in range(97,123):
            newwd[i]=chr(ch)
            if(newwd in a and newwd==edword):
                flag=True
                ans=m[wd]+1
                break
            if(newwd in a and newwd not in m):
                q.append(newwd)
                m[newwd]=m[wd]+1
        if(flag):
            break
    if(flag):
        break
print(ans)
             