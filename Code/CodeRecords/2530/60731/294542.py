s=input()
t=input()
res1=''
res2=''
res=''
for i in range(len(s)):
    num=t.count(s[i])
    for j in range(num):
        res1+=s[i]
for k in range(len(t)):
    if t[k] not in s:
        res2+=t[k]
res=res1+res2
print(res)