s=input()
t=input()
d={c:0 for c in s}
ans=""
for i in list(t):
    if i in list(s):
        d[i]+=1
    else:
        ans+=i
for c in d:
    ans+=c*d[c]
print(ans)


print(result)
