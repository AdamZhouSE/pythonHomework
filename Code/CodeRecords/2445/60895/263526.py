str=input().split(',')
s=str[0].lstrip('s = "')
s=s.rstrip('"')
s=list(s)
t=str[1].lstrip('t = "')
t=t.rstrip('"')
t=list(t)
for i in range(0,len(t)-1):
    for j in range(i+1,len(t)):
        if ord(t[i])>ord(t[j]):
            t[i],t[j]=t[j],t[i]
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if ord(s[i])>ord(s[j]):
            s[i],s[j]=s[j],s[i]
s=''.join(s)
t=''.join(t)
if s==t:
    print('true')
else:
    print('false')
