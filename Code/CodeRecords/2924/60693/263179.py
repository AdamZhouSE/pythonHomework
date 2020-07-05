def write_essays(a,b,n,r,avg):
    if sum(a)>=avg*n:
        return 0
    dis=avg*n-sum(a)
    res=0
    for i in range(n):
        a[i]=r-a[i]
    dict={}
    for i in range(n):
        dict[b[i]]=dict.get(b[i],[])+[a[i]]
    for x in sorted(dict.keys()):
        if sum(dict.get(x))>=dis:
            return res+x*dis
        dis-=sum(dict.get(x))
        res+=x*sum(dict.get(x))

n_r_avg=input().split()
n,r,avg=int(n_r_avg[0]),int(n_r_avg[1]),int(n_r_avg[2])
a,b=[],[]
for _ in range(n):
    inp=input().split()
    a.append(int(inp[0]))
    b.append(int(inp[1]))
print(write_essays(a,b,n,r,avg))