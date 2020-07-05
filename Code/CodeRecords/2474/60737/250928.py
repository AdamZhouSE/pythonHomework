def match_par(s):
    chars = list(s)
    dp = [0] * len(chars)
    pre = 0
    res = 0
    for i in range(1, len(chars)):
        if chars[i] == ')':
            pre=i-dp[i-1]-1
            if pre >= 0 and chars[pre] == '(':
                dp[i]=dp[i-1]+2+(dp[pre-1] if pre>0 else 0)
        res=max(res,dp[i])
    return res


if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        print(match_par(s))
        t -= 1
        