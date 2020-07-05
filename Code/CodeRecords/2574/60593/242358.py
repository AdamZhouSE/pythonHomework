import math
t=int(input())
n=[0]*t
maxx=0
for tt in range(t):
    n[tt]=int(input())
    maxx=max(maxx,n[tt])
prime=[]
i=2
cnt=0
while(cnt<maxx):
    flag=True
    for j in range(2,i):
        if(i%j==0):
            flag=False
            break
    if(flag):
        prime.append(i)
        cnt+=1
    i+=1
for i in range(t):
    print(prime[n[i]-1]**2+1)