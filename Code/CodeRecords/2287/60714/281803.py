T = int(input())
for i in range(0, T):
    n = int(input())
    nums = [int(x) for x in input().split()]
    ans = []
    for j in range(0, n):
        k = j + 1
        flag = False
        while k < n:
            if nums[k] >= nums[j]:
                flag = True
                ans.append(nums[k])
                break
            k += 1
        if not flag:
            ans.append(-1)
    for item in ans[: -1]:
        print(item, end=" ")
    print(ans[-1])
