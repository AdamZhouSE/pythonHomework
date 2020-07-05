n=int(input())
a=input().split(' ')
num=[]
sum=0
for i in range(len(a)):
    num.append(int(a[i]))
    sum=sum+int(a[i])
if sum%3!=0:
    print(0)
else:
    currsum=num[0]
    onethird=sum/3
    ans=0
    psonethird=0
    if num[0]==onethird:
        psonethird=1
    for i in range(1,n-1):
        currsum=currsum+num[i]
        if currsum==onethird*2:
            ans=ans+psonethird
        if currsum==onethird:
            psonethird=psonethird+1
    print(ans)
