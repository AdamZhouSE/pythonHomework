N=int(input())
res=0
for i in range(0,N+1):
    s=list(str(i))
    for j in range(0,len(s)):
        if s.count(s[j])>1:
            res=res+1
            break
print(res)