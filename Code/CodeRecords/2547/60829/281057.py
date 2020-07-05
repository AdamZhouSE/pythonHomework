n=int(input())
for p in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    c=int(input())
    res=[]
    for i in range(len(b)-1):
        for j in range(i+1,len(b)):
            if b[i]-b[j]==c or b[j]-b[i]==c:
                x=[]
                x.append(b[i])
                x.append(b[j])
                if not x in res:
                    res.append(x)
    print(len(res))