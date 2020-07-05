def solve():
    n=int(input())
    tool=find2(n)
    print(n^tool)


def find2(n):
    res=1
    while(res<=n):
        res=2*res
    res-=1
    return res

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()