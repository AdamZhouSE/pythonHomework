N, S = [int(x) for x in input().split()]
nums = []
for i in range(N):
    nums.append(eval(input()))


def getAns(idx):
    res = 0
    sz = N - idx
    while res <= sz - 2:
        if sum(nums[idx:idx + res // 2 + 1]) <= S and sum(nums[idx + res // 2 + 1:idx + res + 2]) <= S:
            res += 2
        else:
            break
    return res


lst = []
for i in range(N):
    ans = getAns(i)
    lst.append(ans)
    print(ans)