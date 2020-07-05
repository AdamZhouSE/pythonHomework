def solve():
    input()
    coins=list(map(int,input().split()))
    cset=set(coins)
    res=0
    for coin in cset:
        num=coins.count(coin)
        if num>res:
            res=num
    print(res)

if  __name__ == '__main__' :
    solve()