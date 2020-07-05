s1=input()
s1=list(s1)
s1.sort()
s1=''.join(s1)
s2=input()
s2=list(s2)
ans=False
for i in range(len(s2)-len(s1)+1):
    s=s2[i:i+len(s1)]
    s.sort()
    s=''.join(s)
    if s1==s:
        ans=True
        break
print(ans)