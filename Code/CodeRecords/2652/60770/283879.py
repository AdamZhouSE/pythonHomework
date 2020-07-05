def solve():
    c,n,f=map(int,input().split())
    c1=int(c/2)
    stds=[]
    for i in range(n):
        stds.append(list(map(int,input().split())))
    stds.sort(key=lambda x:x[0],reverse=True)
    for i in range(c1,n-c1-1):
        left=stds[:i]
        right=stds[i+1:]
        cur=stds[i][1]
        left.sort(key=lambda x:x[1])
        right.sort(key=lambda x:x[1])
        cur+=sum(map(lambda x:x[1],left[:c1]))
        cur+=sum(map(lambda x:x[1],right[:c1]))
        if cur<=f:
            print(stds[i][0],end='')
            return
    print(-1,end='')

if  __name__ == '__main__' :
    solve()
