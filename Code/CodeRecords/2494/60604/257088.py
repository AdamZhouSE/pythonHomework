x=input()
x="s="+x
exec(x)
res=0
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]>2*s[j]:
            res+=1
print(res)