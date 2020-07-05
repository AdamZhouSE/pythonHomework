times = int(input())
for i in range(times):
    length = int(input())
    nums = sorted(list(map(int, input().split(" "))))
    k = int(input())
    print(nums[k-1])
