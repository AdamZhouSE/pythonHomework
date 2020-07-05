res=0
s=input().split(",")
for i in range(len(s)): s[i]=int(s[i])
son=[]

def next_(tl):
    if tl not in son:
        son.append(tl)
    if len(tl)>1:
        for i in range(len(tl)):
            thisl=tl[:]
            thisl.pop(i)
            next_(thisl)
    return 0

next_(s)

for i in range(len(son)):
    res+=(max(son[i])-min(son[i]))
print(res%(10**9+7))
