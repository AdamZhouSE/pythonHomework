# string 9
def test():
    string = input()
    dp = [[0] * len(string) for _ in range(0, len(string))]
    for i in range(0, len(string)):
        for j in range(0, len(string)):
            dp[i][j] = j - i + 1
    for i in range(1, len(string)):
        for j in range(i - 1, -1, -1):
            l = i - j + 1
            dp[j][i] = l
            for k in range(j, i):
                if check(string, j, k, k + 1, i):
                    dp[j][i] = min(dp[j][i], dp[j][k] + 2 + cal(l // (k - j + 1)))
                else:
                    dp[j][i] = min(dp[j][i], dp[j][k] + dp[k + 1][i])
    print(dp[0][len(string) - 1])


def check(string, l1, l2, l3, l4):
    length = l2 - l1 + 1
    if (l4 - l3 + 1) % (l2 - l1 + 1) != 0:
        return False
    for i in range(l3, l4 + 1):
        if string[i] != string[i - length]:
            return False
    return True


def cal(n):
    return len(str(n))

test()
