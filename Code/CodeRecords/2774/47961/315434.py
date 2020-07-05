a=int(input())
for i in range(0,a):
    b=[int(i) for i in input().split()]
    c=[int(i) for i in input().split()]
    c.sort()
    sums=0
    for j in range(0,b[0]):
        sums=sums+c[j]
        if sums>b[1]:
            print(j)
            break