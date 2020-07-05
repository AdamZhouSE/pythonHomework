n=int(input())
d=list(map(int,input().split()))
s,t=map(int,input().split())
distanc1,distanc2=0,0
tmp=s
while tmp!=t:
    distanc1+=d[tmp-1]
    tmp=tmp+1 if tmp<n else 1
while tmp!=s:
    distanc2+=d[tmp-1]
    tmp=tmp+1 if tmp<n else 1
print(min(distanc1,distanc2))