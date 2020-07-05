s=list(eval(input()))
s.sort()
res=0
for i in range(len(s)-1):
    res=max(res,s[i+1]-s[i])
print(res)