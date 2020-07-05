import math
t=int(input())
n=[0]*t
maxx=0
for tt in range(t):
    n[tt]=int(input())
    maxx=max(maxx,n[tt])
prime=[]
for i in range(2,maxx+1):
    flag=True
    for j in range(2,math.ceil(maxx**0.5)):
        if(i%j==0):
            flag=False
            break
    if(flag):
        prime.append(i)
for i in range(t):
    print(prime[n[i]-1]**2+1)