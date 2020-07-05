import math


def solve():
    input()
    box=list(map(int, input().split()))
    b=set(box)
    res=0
    rest=0
    current=0
    while len(b)!=0:
        current=min(b)
        b.remove(current)
        num=box.count(current)
        if num>res:
            if num>res+rest:
                num=num-res-rest
                rest=0
                new=math.ceil(num/(current+1))
                rest=new*(current+1)-new
                res+=new
            else:
                rest-=(num-res)
    print(res)

if  __name__ == '__main__' :
    solve()