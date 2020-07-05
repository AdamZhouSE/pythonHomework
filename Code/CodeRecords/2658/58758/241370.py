count = int(input())
ans = []
for i in range(0, count):
    nums = input().split()
    num_ints = int(nums[0])
    factor = int(nums[1])
    nums = input().split()
    result = 0
    for j in range(0, num_ints):
        if int(nums[j]) % factor == 0:
            result = result | int(nums[j])
    ans.append(result)
for k in ans:
    print(k)
