n=int(input())
for p in range(n):
    a=[int(x) for x in input().split(" ")]
    b=[]
    c=[]
    for i in range(0,a[0]):
        aa=[int(x) for x in input().split(" ")]
        for j in range(a[0]):
            b.append(aa[j])
    for i in range(0,a[0]):
        aa=[int(x) for x in input().split(" ")]
        for j in range(a[0]):
            c.append(aa[j])
    count=0
    for i in range(0,len(b)):
        for j in range(0,len(c)):
            if b[i]+c[j]==a[1]:
                count += 1
    print(count)