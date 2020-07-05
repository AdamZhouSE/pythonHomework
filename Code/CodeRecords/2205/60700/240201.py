tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    n = int(nums[i]) // 2
    shake = [1, 1]
    for j in range(2, n+1):
        count = 0
        for k in range(j):
            count += shake[k] * shake[j-k-1]
        shake.append(count)
    print(shake.pop())
