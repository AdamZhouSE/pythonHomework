n=int(input())

temp=[int(x) for x in input().split(' ')]
ran=[x for x in range(1,n+1)]
aim=0
count=0
ind=0
same=False
while(not same):
    same=True
    l=min(temp)
    u=max(temp)
    for x in ran:
        if x not in temp:
            aim=x
            break
    if(l<=0):
        ind=temp.index(l)
        count+=(aim-l)
        temp[ind]=aim
    elif(u>n):
        ind=temp.index(u)
        count+=(u-aim)
        temp[ind]=aim
    else:
        for i in range(1,n+1):
            if(temp.count(i)>=2):
                ind=temp.index(i)
                count+=abs(i-aim)
                temp[ind]=aim
    for i in range(1,n+1):
        if(i not in temp):
            same=False
print(count)               