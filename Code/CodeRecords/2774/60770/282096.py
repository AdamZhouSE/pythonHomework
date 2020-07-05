def solve():
    n,k=map(int,input().split())
    price=list(map(int,input().split()))

    res=0
    def dfs(rest,num,path):
        nonlocal res
        for i in range(n):
            if price[i]>rest or i in path:
                continue
            dfs(rest-price[i],num+1,path+[i])
        if num>res:
            res=num

    dfs(k,0,[])
    print(res)
if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()