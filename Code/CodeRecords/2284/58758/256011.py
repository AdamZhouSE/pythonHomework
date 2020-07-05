num_test = int(input())
ans = []
for i in range(0, num_test):
    n = int(input())
    nums = [int(x) for x in input().split()]
    result = 0
    for k in range(0, len(nums)-1):
        for j in range(len(nums)-1, k-1, -1):
            if nums[k] < nums[j]:
                if j-k > result:
                    result = j-k
                break
    ans.append(result)
for i in ans:
    print(i)
