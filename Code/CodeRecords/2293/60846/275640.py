t=int(input())
while t:
    n=int(input())
    nums=[int(x) for x in input().split()]
    nums.sort()
    i=int(input())
    print(nums[i-1])
    t-=1