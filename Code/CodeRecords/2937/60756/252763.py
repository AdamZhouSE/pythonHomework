s=list(input())
std=list("CODEFESTIVAL2016")
ans=0
for i in range(16):
    if s[i]!=std[i]:
        ans+=1
print(ans)