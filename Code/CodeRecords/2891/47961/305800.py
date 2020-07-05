a=int(input())
b=[int(i) for i in input().split()]
maxnum=max(b)
sums=0
for i in range(0,a):
    sums=sums+maxnum-b[i]
print(sums)