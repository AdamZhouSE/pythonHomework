num=list(input().split(" "))
n=int(num[0])
p=int(num[1])
tem=list(input().split(" "))
for i in range(n):
    tem[i]=int(tem[i])
m=int(input())
number=[]
for i in range(m):
    a=list(input().split(" "))
    for j in range(len(a)):
        a[j]=int(a[j])
    number.append(a)
ans=0
for i in range(len(number)):
    ans=0
    if number[i][0]==1:
        for k in range(number[i][1]-1,number[i][2]):
            tem[k]=tem[k]*number[i][3]
    if number[i][0]==2:
        for k in range(number[i][1]-1,number[i][2]):
            tem[k]=tem[k]+number[i][3]
    if number[i][0]==3:
        for k in range(number[i][1]-1,number[i][2]):
            ans+=tem[k]
        ans=ans%p
        print(ans)