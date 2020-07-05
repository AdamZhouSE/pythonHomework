def compress_songs(a,b,n,m):
    if sum(b)>m:return -1
    if sum(a)<=m:return 0
    dis=sum(a)-m
    compre=[]
    res=0
    for i in range(n):
        compre.append(a[i]-b[i])
    compre.sort(reverse=True)
    for x in compre:
        if x>=dis:return res+1
        dis-=x
        res+=1

n_m=input().split()
n,m=int(n_m[0]),int(n_m[1])
a,b=[],[]
for i in range(n):
    inp=input().split()
    a.append(int(inp[0]))
    b.append(int(inp[1]))
print(compress_songs(a,b,n,m))