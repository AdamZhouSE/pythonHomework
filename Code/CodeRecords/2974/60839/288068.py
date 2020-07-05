def isPositive(st):
    judge=False
    if len(st)%2==1:
        temp=True
        for i in range(0,len(st)//2):
            if st[i]!=st[len(st)-1-i]:
                temp=False
        if temp:
            judge=True
    return judge

def func(left,right)->int:
    lis1=[]
    lis2=[]
    for i in range(0,len(left)):
        for j in range(i,len(left)):
            lis1.append(left[i:j+1])
    se=set(lis1)
    lis1=list(se)
    for i in range(0,len(right)):
        for j in range(i,len(right)):
            lis2.append(right[i:j+1])
    se=set(lis2)
    lis2=list(se)
    sum1=0
    sum2=0
    for i in lis1:
        if isPositive(i):
            sum1=sum1+1
    for i in lis2:
        if not isPositive(i):
            sum2=sum2+1
    return sum1*sum2


n=int(input())
s=input()
ans=[]
for i in range(0,n-1):
    l=s[0:i+1]
    r=s[i+1:]
    ans.append(func(l,r))

print(max(ans))