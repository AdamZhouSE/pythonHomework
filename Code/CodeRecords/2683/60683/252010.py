import string

values = dict(zip(string.ascii_lowercase, [x for x in range(1, 27)]))


def lenOfMaxIncreSubseq(s):
    sz = len(s)
    dp = [1] * sz
    for j in range(sz):
        for k in range(j):
            if values[s[j]] > values[s[k]] and dp[k] + 1 > dp[j]:
                dp[j] = dp[k] + 1
    return max(dp)


T = eval(input())
for i in range(T):
    s = input()
    print(lenOfMaxIncreSubseq(s))