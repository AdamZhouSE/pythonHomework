length = int(input())
nums = list(map(int, input().split(" ")))
f = [[0 for i in range(length)] for j in range(length)]
root = [[0 for i in range(length)] for j in range(length)]
for i in range(length):
    f[i][i] = nums[i]
    root[i][i] = i


def dfs(l, r):
    if l > r:
        return 1
    elif l == r:
        root[l][r] = l
        return nums[l]
    else:
        if f[l][r]:
            return f[l][r]
        else:
            for i in range(l, r + 1):
                temp = dfs(l, i-1) * dfs(i + 1, r) + nums[i]
                if temp > f[l][r]:
                    f[l][r] = temp
                    root[l][r] = i
            return f[l][r]


def pri(l, r):
    if l > r:
        return
    else:
        print(root[l][r]+1, "", end="")
        pri(l, root[l][r] - 1)
        pri(root[l][r] + 1, r)


dfs(0, length - 1)
print(f[0][length - 1])
pri(0, length - 1)
