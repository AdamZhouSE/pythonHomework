from functools import reduce


def solve():
    n=int(input())
    nums=list(map(int,input().split()))
    k=int(input())
    mul=reduce(lambda x,y:x*y,nums)
    res=mul%k
    print(res)

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()