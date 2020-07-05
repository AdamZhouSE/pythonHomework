n=int(input())
temp=[int(x) for x in input().split(' ')]
res=[]

for i in range(n):
    res.append(temp[i])
    out=[]
    count=0
    for j in range(len(res)):
        for k in range(len(res)-j):
            pre=temp[k:k+j+1]
            if(pre not in out):
                out.append(pre)
    count=len(out)
    print(count)
        