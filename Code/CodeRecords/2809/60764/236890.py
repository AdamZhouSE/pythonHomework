a=int(input())
n=list(map(int,input().split()))
long=0
width=0
for i in range(int(a/2)):
    long+=min(n)
    n.remove(min(n))
for j in range(len(n)):
    width+=n[j]
res=int(pow(long,2))+int(pow(width,2))
print(res)