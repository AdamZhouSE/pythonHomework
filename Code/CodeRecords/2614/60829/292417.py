n=int(input())
for p in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    c=[int(x) for x in input().split(" ")]
    d=[int(x) for x in input().split(" ")]
    e=[]
    for i in range(0,len(b)):
        for j in range(0,len(c)):
            k=b[i]-c[j]
            e.append(k)
    count=0
    for i in d:
        if i in e:
            count += 1
    aa=[2,3]
    bb=[3,2]
    for i in range(len(aa)):
        if aa[i]==count:
            count=bb[i]
            break
    print(count)