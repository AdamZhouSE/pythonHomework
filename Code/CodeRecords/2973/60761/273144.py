def matchnum(s,code):
    ans=0
    for i in range(0,len(s)-7):
        temp=s[i:i+8]
        k=1
        for j in code:
            if code.count(j)!=temp.count(j):
                k=0
                break
        ans+=k
    return ans
                
s=input()
n=int(input())
ans=0
for i in range(n):
    code=input()
    ans=ans+matchnum(s,code)
print(ans)