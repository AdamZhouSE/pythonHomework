def find():
    global n
    f=[0 for i in range(43)]
    loc=[-1 for i in range(8)]
    cnt=1
    for i in range(n):
        if(vis[i]!=0 or f[a[i]]!=0):
            continue
        else:
            if(cnt<7):
                f[a[i]]=cnt
                loc[cnt]=i
                cnt+=1
        if(f[4]==1 and f[8]==2 and f[15]==3 and f[16]==4 and f[23]==5 and f[42]==6):
            for i in range(1,7):
                vis[loc[i]]=1
            return True
    return False
dd=0
n=int(input())
a=list(map(int,input().split()))
vis=[0 for i in range(n)]
while(True):
    if(find()==False):
        break
    dd+=6
print(len(a)-dd)
