s=list(input())
n=len(s)
boy=0
girl=0
for i in range(n):
    if (s[i]=='b') or (i+1<n and s[i+1]=='o') or (i+2<n and s[i+2]=='y'):
        boy+=1
    if (s[i]=='g') or (i+1<n and s[i+1]=='i') or (i+2<n and s[i+2]=='r' ) or (i+3<n and s[i+3]=='l'):
        girl+=1
print(boy)
print(girl)