st=input()[5:-1].split('\", t = \"')
s=st[0]
t=st[1]
if len(s)!=len(t):
    print('false')
    exit()
for i in range(len(s)):
    if t.find(s[i])==-1:
        print('false')
        exit()
    t=t[:t.index(s[i])]+t[t.index(s[i])+1:]
print('true')