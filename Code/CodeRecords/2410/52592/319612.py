inp = eval(input())
difference = int(input())
arr=[]
for i in range(len(inp)):
    arr.append(inp[i])
dp=dict()
for n in arr:
    dp[n]=(dp[n-difference] if n-difference in dp else 0)+1
print(max(dp.values()))