s=list(input())
all=[]
for i in range(len(s)):
    t=s[0]
    s.pop(0)
    s.append(t)
    tem="".join(s[::])
    all.append(tem)
all.sort()
ans=""
for i in range(len(all)):
    ans=ans+all[i][-1]
print(ans)
