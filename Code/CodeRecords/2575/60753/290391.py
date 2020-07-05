import sys
s=sys.stdin.read()
n=len(s)
ans=[0]*n
for i in range(1,n):
    if s[i]==s[i-1]:
        ans[i]=1-ans[i-1]
    else:
        ans[i]=ans[i-1]
print(ans)