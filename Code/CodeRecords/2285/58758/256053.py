num_test = int(input())
ans = []
for m in range(0, num_test):
    n = int(input())
    nums = [int(x) for x in input().split()]
    i = 0
    result = []
    while i < len(nums):
        j = i+1
        while j < len(nums) and nums[j-1] <= nums[j]:
            j += 1
        if j != i+1:
            result.append(i)
            result.append(j-1)
        i = j
    ans.append(result)
for obj in ans:
    for i in range(0, len(obj)-2, 2):
        print(f'({obj[i]} {obj[i+1]})', end=' ')
    print(f'({obj[len(obj)-2]} {obj[len(obj)-1]})')
