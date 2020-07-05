n = int(input())
for i in range(0, n):
    m = int(input())
    nums = [int(x) for x in input().split()]
    temp = nums[-1]
    ans = [temp]
    for j in range(m - 2, -1, -1):
        if nums[j] >= temp:
            temp = nums[j]
            ans.insert(0, temp)
    for j in range(0, len(ans) - 1):
        print(ans[j], end=" ")
    print(ans[-1])
