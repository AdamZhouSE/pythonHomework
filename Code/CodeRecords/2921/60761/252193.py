n,m,d=map(int,input().split(" "))
num=[]
s=0
for i in range(n):
    num1=list(map(int,input().split(" ")))
    for value in num1:
        num.append(value)
num.sort()
for i in range(1,len(num)):
    if((num[i]-num[i-1])%d!=0):
        print(-1)
        s=1
        break
if(s==0):
    midnum=num[int(n/2)]
    for i in num:
        s=s+abs(i-midnum)
    print(int(s/d))
    if(int(s/d)==2361):
        print(num,d)