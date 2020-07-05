#动态规划，复习的时候好好看
def longest_substring(a):
    s=list(a)
    n=len(s)
    dp=[1]*n
    for i in range(n):
        for j in range(i):
            if ord(s[j])<ord(s[i]):
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)


T=int(input())
for i in range(T):
    s=input()
    print(longest_substring(s))