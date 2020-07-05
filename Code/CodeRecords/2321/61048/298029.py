
def numop30():
    str_in=input().split(',')
    set=[int(x) for x in str_in]
    N=int(input())
    S=str(N)
    maxindex=len(str(N))
    dp=[0]*maxindex
    for i in range(maxindex - 1, -1, -1):
        for d in set:
            if d < int(S[i]):
                dp[i] += len(set) ** (maxindex- i - 1)
            elif d == int(S[i]):
                dp[i] += dp[i + 1]
    print(dp[0]+sum(len(set)**i for i in range(1,maxindex)))
    return 0

numop30()