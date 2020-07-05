n,m = [int(i) for i in input().split(' ')]
a = [int(i) for i in input().split(' ')]
x = 0
while(x<m):
    x += 1
    temp = [int(i) for i in input().split(' ')]
    if temp[0] == 1:
        l,r,k,d = [int(i) for i in input().split(' ')]
        for i in range(l-1,r):
            a[i] += K + (i - l + 1)*d
    else:
        p = [int(i) for i in input().split(' ')][1]
        print(a[p-1])
        