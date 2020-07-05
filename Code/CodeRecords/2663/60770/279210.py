def solve():
    n=int(input())
    res=0
    nextplus=3
    for i in range(n):
        res+=nextplus
        nextplus+=4
    print(res)

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()