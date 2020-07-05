t = int(input())
s=list(input())
ans=[s[1],s[0],s[2]]
for j in range(t-1):
    s=list(input())
    index=s.index(s[0])
    if s[1]!='*':
        ans.insert(index,s[1])
        if s[2]!='*':
            ans.insert(index+2,s[2])
print(''.join(ans))