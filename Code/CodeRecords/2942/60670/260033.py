n=int(input())
strs=input().split()
strs=sorted(strs,reverse=True)
ans=""
for s in strs:
    ans+=s
print(ans)