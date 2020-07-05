a=int(input())
b=[int(t) for t in input().split()]
b.insert(0,0)
count=0
minum=0
for i in range(1,a+1):
    count+=(b[i-1]-b[i])
    minum=min(count,minum)
print(-1*minum)