n,m,d=map(int,input().split())
num=[]
for i in range(n):
    num+=list(map(int,input().split()))
num.sort()
count=0
for i in range(len(num)):
    temp=0
    conti=True
    for j in num:
        if abs(j-num[i])%d!=0:
            conti=False
            break
        else:
            temp+=int(abs(j-num[i])/d)
    if(i==0):
        count=temp
    count=min(temp,count)
    if not conti:
        print(-1)
        break
    if i==len(num)-1:
        print(count)