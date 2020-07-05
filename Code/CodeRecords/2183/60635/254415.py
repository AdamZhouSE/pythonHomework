count=int(input())
for i in range(count):
    line=int(input())
    dp=[0]*line
    curr=1
    len=2
    for i in range(line):
        for j in range(len):
            dp[i]+=curr
            curr+=1
        len+=2
    print(dp[-1])
    