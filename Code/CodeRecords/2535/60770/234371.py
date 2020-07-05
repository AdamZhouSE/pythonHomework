def solve():
    nums = list(map(int, input()[1:-1].split(',')))
    res=0
    while len(nums)!=0:
        nums=nums[findMin(nums)+1:]
        res+=1
    print(res)

def findMin(nums=[]):
    min=nums[0]
    index=0
    for i in range(1,len(nums)):
        if nums[i]<min:
            index=i
            min=nums[i]
    return index

if  __name__ == '__main__' :
    solve()