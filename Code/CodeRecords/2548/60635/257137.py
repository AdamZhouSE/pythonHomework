tests = int(input())
for t in range(tests):
    src=input()
    n=len(src)
    k=int(input())
    dp=['']*n
    curr=0
    count=0
    tmp=src[0]
    while count<k:
        if curr<n-1:
            curr += 1
            tmp+=src[curr]
        count=len(set(tmp))
    dp[curr]=tmp
    for i in range(curr+1,n):
        tmp=dp[i-1]+src[i]
        while len(set(tmp))!=k:
            tmp=tmp[1:]
        dp[i]=tmp
    lengths=[len(s) for s in dp]
    print(max(lengths))