def find():
    global n
    f=[False for i in range(43)]
    for i in range(n):
        if(vis[i]!=0):
            continue
        else:
            f[a[i]]=True
    if(f[4]and f[8]and f[16]and f[23]and f[42]):
        return True
    return False
ans=0
n=int(input())
a=list(map(int,input().split()))
vis=[0 for i in range(n)]
while(True):
    if(find()):
        break
    ans+=6
print(ans)
