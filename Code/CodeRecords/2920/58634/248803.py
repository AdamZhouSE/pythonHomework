n,k = map(int, input().split())
nums = [int(i) for i in input().split(" ")]
nums.sort()
if n==k:
    print(0)
else:
    d = n//k#每个序列的元素个数
    minInt = nums[n-1] - nums[0]
    for i in range(k):
        minInt = min(nums[i+(d-1)*k]-nums[i],minInt)
    print(minInt)

# k =2 d = 3 >0 2 4  1 3 5