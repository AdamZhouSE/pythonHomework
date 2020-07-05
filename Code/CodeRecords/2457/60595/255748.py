def Test():
    f=[]
    ne=[]
    po=[]
    ru=[]
    root=0
    for i in range(0,5):
        line=[]
        for j in range(1000):
            line.append(0)
            ne.append(0)
            po.append(0)
            ru.append(0)
        f.append(line)
    def dp(x):
        i=po[x]
        while(i!=0):
            dp(i)
            f[1][x] = max(max(f[1][x], f[0][i] + f[1][x]), f[0][i])
            f[0][x] = max(max(f[0][x], f[1][i] + f[0][x]), max(f[1][i], f[0][i]))
            i=ne[i]
    n=int(input())
    for i in range(1,n+1):
        f[1][i]=int(input())
    for i in range(1,n+1):
        b,a=map(int,input().split())
        ru[b]=ru[b]+1
        ne[b]=po[a]
        po[a]=b
    for i in range(1,n+1):
        if(ru[i]==0):
            root=i
            break
    dp(root)
    print(max(f[1][root],f[0][root]),end="")
if __name__ == "__main__":
    Test()