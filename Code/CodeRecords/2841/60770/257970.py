def solve():
    n,m=map(int,input().split())
    nums=list(map(int,input().split()))
    def change(p,b):
        nums[p-1]=b
    for i in range(m):
        p,b=map(int,input().split())
        change(p,b)
        print(getV(n,0,nums))


def getV(n,state,nums):
    if n==0:
        return nums[0]
    if state==0:
        nex=list(map(lambda x,y:x|y,nums[0::2],nums[1::2]))
        return getV(n-1,1,nex)
    else:
        nex=list(map(lambda x,y:x^y,nums[0::2],nums[1::2]))
        return getV(n-1,0,nex)

if  __name__ == '__main__' :
    solve()