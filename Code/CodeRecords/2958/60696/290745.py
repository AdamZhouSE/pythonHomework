INT_MAX = 2147483647


def check(l, r, k):
    if (r-l+1) % k != 0:
        return False
    for i in range(l, r-k+1):
        if string[i-1] != string[i+k-1]:
            return False
    return True


def cnt(length, k):
    if length // k < 10:
        return 1
    elif length // k < 100:
        return 2
    else:
        return 3


if __name__ == '__main__':
    string = input()
    n = len(string)
    dp = [[INT_MAX]*(1+n) for i in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            dp[i][j] = abs(j-i) + 1
    for length in range(2, n+1):
        for l in range(1, n+2-length):
            for k in range(2, length):
                dp[l][l+length-1] = min(dp[l][l+length-1], dp[l][l+k-1] + dp[l+k][l+length-1])
            for k in range(1, length):
                if length % k != 0:
                    continue
                if check(l, l+length-1, k):
                    dp[l][l+length-1] = min(dp[l][l+length-1], dp[l][l+k-1]+cnt(length, k) + 2)
    print(dp[1][n])