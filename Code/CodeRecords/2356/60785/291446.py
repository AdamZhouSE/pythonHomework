t=int(input())
for test in range(t):
    n=int(input())
    nums = [int(i) for i in input().split()]
    for i in range(1,n-1):
        if sorted(num[0:i+1])[-1]==nums[i] and sorted(num[i:])[0]==nums[i]:
            print(nums[i])
            break