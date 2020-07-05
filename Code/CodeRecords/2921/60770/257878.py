def solve():
    n,m,d=map(int,input().split())
    nums=[]
    for i in range(n):
        nums+=list(map(int,input().split()))
    middle=getMiddle(nums)
    res=0
    for i in range(len(nums)):
        dif=abs(nums[i]-middle)
        if dif%d!=0:
            print(-1)
            return
        res+=int(dif/d)
    print(res)


def getMiddle(nums=[]):
    nums.sort()
    return nums[int(len(nums)/2)]

if  __name__ == '__main__' :
    solve()