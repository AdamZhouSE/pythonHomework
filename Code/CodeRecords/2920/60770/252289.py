from functools import reduce


def solve():
    n,m=map(int,input().split())
    nums=list(map(int,input().split()))
    if n<=1 or n==m:
        print(0)
        return

    difs=[]
    for i in range(n-1):
        difs.append(nums[i+1]-nums[i])
    for i in range(m-1):
        difs.remove(max(difs))
    res=reduce(lambda x,y:x+y,difs)
    print(res)

if  __name__ == '__main__' :
    solve()
