k, n = [int(x) for x in input().split(', ')]
ans = []


def backtrack(target, start, count, nums):
    if count == k:
        if target == 0:
            ans.append(nums)
        return
    if start > target:
        return
    for i in range(start, 9):
        backtrack(target-i, i+1, count+1, nums+[i])


backtrack(n, 1, 0, [])
print(ans)
