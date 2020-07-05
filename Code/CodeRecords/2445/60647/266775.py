b=input()
c=b.split()
d=[]
for i in range(len(c)):
    if c[i]=='=':
        d.append(c[i+1])
s=d[0]
t=d[1]
def isAnagram(s, t):
    if len(s) != len(t):
        return 'false'
    dic1 = {}
    dic2 = {}
    for i in range(len(s)):
        if s[i] not in dic1:
            dic1[s[i]] = 1
        else:
            dic1[s[i]] += 1
    for j in range(len(t)):
        if t[j] not in dic2:
            dic2[t[j]] = 1
        else:
            dic2[t[j]] += 1
    for key in dic1.keys():
        if key not in dic2.keys() or dic1[key] != dic2[key]:
            return 'false'
    return 'true'
res=isAnagram(s,t)
print(res)
