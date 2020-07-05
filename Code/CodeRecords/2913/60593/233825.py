n=int(input())
arr=list(map(int,input().split()))
m=0
addup=0
for i in arr:
    addup+=i
    if(m<i):
        m=i
if(addup%2!=0):
    print('NO')
else:
    print('YES'if(m<=addup-m)else'NO')