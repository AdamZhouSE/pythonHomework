a=int(input())
b=[int(i) for i in input().split()]
sums=0
for i in range(0,len(b)):
    sums=sums+b[i]
print(format(sums/a,'.6f'))