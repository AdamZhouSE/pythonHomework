a=int(input())
b=[int(t) for t in input().split()]
b.sort()
count=0
total=(b[0]-1)*a
for i in range(a):
    count+=(b[i])
    total+=(i+1)
print(total-count)
