cases=int(input())
req=[]
for c in range(cases):
    req.append(int(input()))
num=max(req)
dp=[0]*num
dp[0]=1
adder=1
for i in range(1,num):
    adder+=2*i+1
    dp[i]=dp[i-1]+adder
for r in req:
    print(dp[r-1])