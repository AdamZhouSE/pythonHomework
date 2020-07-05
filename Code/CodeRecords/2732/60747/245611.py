import math
n=int(input())
result=[]
sum=0
count=0
for k in range(n):
    num=input().split(" ")
    for i in range(len(num)):
        num[i]=int(num[i])
    a=num[0]
    b=num[1]
    c=num[2]
    a = a % c
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a * a) % c
    result.append(ans)
for i in range(len(result)):
    print(result[i])