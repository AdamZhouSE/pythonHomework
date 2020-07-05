n,k = [int(i) for i in input().split()]
a = []
res = 0
for t in range(n):
    a.append([int(i) for i in input().split()])
for i in range(n):
    for j in range(i+1,n):
        x1,y1 = a[i]
        x2,y2 = a[j]
        if x1>x2-k and x1<x2+k and y1>y2-k and y1<y2+k:
            if res==0:
                e1 = k-abs(x1-x2)
                e2 = k-abs(y1-y2)
                res = e1*e2
            else:
                res = -1
                break
print(res)