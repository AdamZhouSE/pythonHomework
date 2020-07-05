def judge(left: int, len_repeat: int, right: int, string: str) -> bool:
    k = left + len_repeat - 1
    while True:
        for i in range(left, len_repeat+left):
            k += 1
            if string[i] != string[k]:
                return False
            else:
                continue
        if k == right:
            return True


def search(string: str) -> int:
    len_str = len(string)
    m = []
    dp = [[2**31-1 for _ in range(len_str)] for _ in range(len_str)]
    for _ in range(10):
        m.append(1)
    for _ in range(10, 100):
        m.append(2)
    m.append(3)
    for i in range(len_str):
        dp[i][i] = 1
    for len_seg in range(2, len_str+1):
        for i in range(len_str):
            j = i + len_seg - 1
            if j >= len_str:
                break
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j])
            for k in range(i, j):
                len_repeat = k - i + 1
                if len_seg % len_repeat != 0:
                    continue
                if judge(i, len_repeat, j, string):
                    dp[i][j] = min(dp[i][j], dp[i][k] + 2 + m[len_seg//len_repeat-1])
    return dp[0][len_str-1]


s = input()
print(search(s))
