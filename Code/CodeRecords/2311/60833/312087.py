def summ(l,r):
    mid=int((r+l)/2)
    s=0
    for i in range(l,mid):
        s+=num[i]
    for i in range(mid+1,r+1):
        s+=num[i]
    num[mid]=s
    if(r-l==2):
        num[r]=0
        num[l]=0
    else:
        summ(l,mid-1)
        summ(mid+1,r)

input()
num=list(map(int,input().split(' ')))
summ(0,len(num)-1)
for i in num:
    print(i,end=' ')