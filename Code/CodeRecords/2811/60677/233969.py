string=input().split()
lim=int(string[0])
lenth=int(string[1])
num=list(range(lenth))
hash=list(range(lim))
flict=0;
for i in range(0,lenth):
    num[i]=int(input())
for i in range(0,lenth):
    if hash[num[i]%lim]==-1:
        print(i+1)
        flict=1
        break
    hash[num[i] % lim] = -1

if flict==0:
    print(-1)