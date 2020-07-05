t=int(input())
for _ in range(t):
    n=int(input())
    nums=input().split(' ');nums=[int(x) for x in nums]
    k=int(input())
    nums.sort()
    print(nums[k-1])