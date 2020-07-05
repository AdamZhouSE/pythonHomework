def at(l):
    
    from bisect import bisect
    jobs=sorted(zip(l[0],l[1],l[2]),key=lambda v:v[1])
    dp=[[0,0]]
    for s,e,p in jobs:
        i=bisect.bisect(dp,[s+1,0])-1
        if dp[i][1]+p>dp[-1][1]:
            dp.append([e,dp[i][1]+p])
    print(dp[-1][1])
if __name__ == '__main__':
    at([eval(input()) for _ in range(3)])
