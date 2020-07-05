t = int(input())
ans=list(input())
for j in range(t-1):
    s=list(input())
    index=ans.index(s[0])
    if s[1]!='*':
        ans.insert(index+1,s[1])
        if s[2]!='*':
            ans.insert(index+2,s[2])
print(''.join(ans),end='')