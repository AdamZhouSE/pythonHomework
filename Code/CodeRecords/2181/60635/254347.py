count=int(input())
for i in range(count):
    index=int(input())
    dp=[0]*index
    dp[0]=2
    adder1=8
    adder2=12
    for i in range(1,index):
        dp[i]=dp[i-1]+adder1
        adder1+=adder2
        adder2+=6
    print(dp[index-1])