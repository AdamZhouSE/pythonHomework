def sets(s1,s):
    if len(s)==len(s1):
        ss.append(s)
        return
    for i in range(len(s1)):
        if s1[i] not in s:
            s+=s1[i]
            sets(s1,s)
            s=s[:-1]

s1=input()
s2=input()
s=""
ss=[]
sets(s1,s)
res=False
for e in ss:
    if e in s2:
        res=True
        break
print(res)
