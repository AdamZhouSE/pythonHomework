n=int(input())
for i in range(n):
    a=[int(x) for x in input().split(" ")]
    b=[int(x) for x in input().split(" ")]
    c=[int(x) for x in input().split(" ")]
    d=[]
    for i in b:
        d.append(i)
    for i in c:
        d.append(i)
    d.sort()
    res=""
    for j in range(len(d)):
        if j<len(d)-1:
            res=res+str(d[j])+" "
        else:
            res=res+str(d[j])+" "
    print(res)