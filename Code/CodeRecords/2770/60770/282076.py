def solve():
    n=int(input())
    st=list(map(int,input().split()))
    en=list(map(int,input().split()))
    res=0
    resli=[]
    def dfs(start,path,num):
        nonlocal res
        nonlocal resli
        for i in range(n):
            if st[i]<start:
                continue
            dfs(en[i],path+[i+1],num+1)
        if num>res:
            res=num
            resli=path[:]

    dfs(0,[],0)
    out=list(map(str,resli))
    print(' '.join(out)+' ')

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()