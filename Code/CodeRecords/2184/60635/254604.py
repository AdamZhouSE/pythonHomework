count=int(input())
for i in range(count):
    index=int(input())
    dp=[0]*index
    adder=7
    dp[0]=3
    for i in range(1,index):
        dp[i]=dp[i-1]+adder
        adder+=4
    print(dp[-1])