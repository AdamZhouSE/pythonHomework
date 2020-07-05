n = int(input())
dp = [[-1] * (n + 1) for i in range(n + 1)]
root = [[0] * (n + 1) for j in range(n + 1)]
mark = True
res = []


def search(f: int, s: int):
    if f > s:
        return 1
    if dp[f][s] == -1:
        ans = 0
        for k in range(f, s + 1):
            ans = search(f, k - 1) * search(k + 1, s) + dp[k][k]
            if ans > dp[f][s]:
                dp[f][s] = ans
                root[f][s] = k

    return dp[f][s]


def preorder(f: int, s: int):
    if f > s:
        return
    else:
        res.append(str(root[f][s]))
        preorder(f, root[f][s] - 1)
        preorder(root[f][s] + 1, s)


scores = input().split(" ")
for i in range(1, n + 1):
    dp[i][i] = int(scores[i - 1])
    root[i][i] = i
print(search(1, n))
preorder(1, n)
print(" ".join(res))