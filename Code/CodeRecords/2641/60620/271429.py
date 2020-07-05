s1=input()
s2=input()
judge=False
def sortf(s):
    if(len(s)==1):
        return s
    slist=[]
    for i in range(len(s)):
        for j in sortf(s[:i]+s[i+1:]):
            slist.append(s[i]+j)
    return slist
r=sortf(s1)
for i in r:
    if(i in s2):
        judge=True
        break
    else:
        continue
print(judge)