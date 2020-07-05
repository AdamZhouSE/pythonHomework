import re
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
dp=[1 for i in range(len(s))]
ans=0
for i in range(1,len(s)):
    for j in range(0,i):
        if(s[j]<s[i]):
            dp[i]=max(dp[i],dp[j]+1)
    ans=max(dp[i],ans)
print(ans)