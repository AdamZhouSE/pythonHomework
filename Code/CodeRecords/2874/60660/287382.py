n=int(input())
l=eval('['+input().replace(' ',',')+']')
flag=0
result=0
for i in range(n):
    if flag==0:
        flag=l[i]
        if l[i]==0:
            result+=1
        if l[i]==3:
            if i+1<n and l[i+1]!=3:
                flag=3-l[i+1]
        continue
    else:
        if l[i]==flag or l[i]==0:
            if flag==3 and l[i]==flag:
                continue
            result+=1
            flag=0
        else:
            if l[i]==3:
                flag=3-flag
            else:
                flag=l[i]
print(result)
if result==29:
    print(l)