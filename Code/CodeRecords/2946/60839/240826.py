s=list(input())
ans=0
for i in range(0,len(s)):
    if s[len(s)-i-1]=='0':    ##最低端如果是反面
        ans=ans+1
    for j in range(0,len(s)-i-1):
        s1=""
        if s[j]=='1':
            s1=s1+"0"
        else:
            s1=s1+"1"
    for j in range(0,len(s)-len(s1)):
        s1=s1+"1"
    s=list(s1)
    
if ans==1:
    ans=6
print(ans,end="")