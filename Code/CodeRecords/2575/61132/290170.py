def evalu2(l):
    sum=0
    Max=0
    for i in l:
        if i=='(':
            sum+=1
        else:
            sum-=1
        Max=max(Max,sum)
    return Max

l=list(input())
n=evalu2(l)//2
s=[1 for i in l]
index=0
sum=0
for i in l:
    if i=='(':
        if sum<n:
            s[index]=0
        sum+=1
    else:
        if sum<=n:
            s[index]=0
        sum-=1

    index+=1
print(s)