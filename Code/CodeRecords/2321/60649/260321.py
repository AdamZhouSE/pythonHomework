D=input().split(",")
s=input()
k=len(s)
dp=[0]*k+[1]
for i in range(k-1,-1,-1):
    for d in D:
        if d<s[i]:
            dp[i]+=len(D)**(k-i-1)
        elif d==s[i]:
            dp[i]+=dp[i+1]
print(dp[0]+sum(len(D)**i for i in range(1,k)))