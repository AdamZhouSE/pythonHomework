times = int(input())
for j in range(times):
    n = int(input())
    nums = [1,1,1]
    for i in range(n-2):
        nums.append(nums[-2]+nums[-3])
    print(nums[-1])