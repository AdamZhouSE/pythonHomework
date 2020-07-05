T = int(input())
for i in range(0, T):
    n = int(input())
    nums = [int(x) for x in input().split()]
    ans = []
    for j in range(0, n):
        k = j
        flag = False
        while k >= 0:
            if nums[k] < nums[j]:
                flag = True
                ans.append(nums[k])
                break
            k -= 1
        if not flag:
            ans.append(-1)
    for item in ans:
        print(item, end=" ")
    print()
