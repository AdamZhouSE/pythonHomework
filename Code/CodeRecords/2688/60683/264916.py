nums = []
ans = [0]


def dfs(begin, end, target):
    if target < 0:
        return
    elif target == 0:
        ans[0] += 1
        return
    elif begin >= end:
        return
    for j in range(begin, end):
        dfs(j + 1, end, target - nums[j])


T = eval(input())
for i in range(T):
    N = eval(input())
    nums = [int(x) for x in input().split()]
    target = eval(input())
    ans[0] = 0
    nums.sort()
    dfs(0, N, target)
    print(ans[0])