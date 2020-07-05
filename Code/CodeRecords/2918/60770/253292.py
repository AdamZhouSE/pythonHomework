import math


def solve():
    input()
    box=list(map(int, input().split()))
    b=set(box)
    res=0
    current=1
    while len(b)!=0:
        current=min(b)
        b.remove(current)
        num=box.count(current)
        if num>res:
            num-=res
            res+=math.ceil(num/(current+1))
    print(res)

if  __name__ == '__main__' :
    solve()