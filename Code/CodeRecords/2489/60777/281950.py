temp=input()
temp=temp[1:len(temp)-1]
temp=[int(x) for x in temp.split(',')]
l=int(input())
u=int(input())
res=0
for i in range(0,len(temp)):
    pre=0
    su=0
    if(temp[i]>=l and temp[i]<=u):
        pre=1
    else:
        pre=0
    su=temp[i]
    for j in range(i+1,len(temp)):
        now=su+temp[j]
        if(now>=l and now<=u):
            pre+=1
        su=now
    res+=pre
print(res)
