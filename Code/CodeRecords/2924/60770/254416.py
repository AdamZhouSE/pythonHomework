from functools import reduce


def solve():
    n,r,avg=map(int,input().split())
    ab=[]
    for i in range(n):
        ab.append(list(map(int,input().split())))
    ab.sort(key=lambda x:x[1])
    total=avg*n
    now=0
    for i in range(n):
        now += ab[i][0]
    rest=total-now
    res=0
    while rest>0:
        while ab[0][0]>=r:
            del ab[0]
        ab[0][0]+=1
        rest-=1
        res+=ab[0][1]

    print(res)

if  __name__ == '__main__' :
    solve()