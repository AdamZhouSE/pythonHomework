a=int(input())
b=[int(t) for t in input().split()]
b.sort()
count=0
total=0
for i in range(1,a):
    if(b[i-1]>=b[i]):
        total+=(b[i-1]-b[i]+1)
        b[i]=b[i-1]+1


print(total-count)

