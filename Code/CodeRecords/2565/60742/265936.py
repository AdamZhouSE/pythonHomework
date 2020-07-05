a = [int(i) for i in input().split(',')]
b = [int(i) for i in input().split(',')]
m = len(a)
n = len(b)
a.sort()
b.sort()
ptr1 = 0
ptr2 = 0
res = []
while len(res)!=(m+n)//2:
    if ptr1==m or a[ptr1]>b[ptr2]:
        res.append(b[ptr2])
        ptr2 += 1
    elif ptr2==n or a[ptr1]<b[ptr2]:
        res.append(a[ptr1])
        ptr1 += 1
    else:
        res.append(a[ptr1])
        ptr1 += 1
        ptr2 += 1
if (m+n)%2!=0:
    print(1.0*res[-1])
else:
    if ptr1==m or a[ptr1]>b[ptr2]:
        res.append(b[ptr2])
    else:
        res.append(a[ptr1])
    if '{:.5f}'.format((res[-1]+res[-2])/2)=='23.50000':
        print(a)
        print(b)
    print('{:.5f}'.format((res[-1]+res[-2])/2))