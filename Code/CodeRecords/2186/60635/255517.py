count=int(input())
req=[]
for i in range(count):
    req.append(int(input()))
index=max(req)
dp=[0]*(index+1)
dp[0]=0
adder=0
for i in range(1,index+1):
    adder+=i
    dp[i]=dp[i-1]+adder
for i in range(count):
    print(dp[req[i]])