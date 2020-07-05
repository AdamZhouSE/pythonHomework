
def solve(nums):
      
    nums.sort()
    mid=len(nums)//2
    res=0
    for n in nums:
        res+=abs(n-nums[mid])
    return res

if __name__ == '__main__':
    a=input()
    b=a.split(",")
    c=list(map(int,b))
    print(solve(c))