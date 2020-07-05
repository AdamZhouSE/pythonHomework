s=input()
ls=s[1:len(s)-1].split(",")
for i in range(len(ls)):
    ls[i]=ls[i][1:len(ls[i])-1]
r=[[ls[0]]]
del ls[0]
i=0
while i<len(ls):
    this=ls[i]
    j=0
    have=False
    while j<len(r):
        subr=r[j]
        for k in range(len(subr)):
            thisr=subr[k]
            if len(thisr)==len(this):
                for a in range(len(this)-1):
                    for b in range(a+1,len(this)):
                        if this[a]==thisr[b] and this[b]==thisr[a]:
                            x1=this[:a]+this[a+1:b]+this[b+1:]
                            x2=thisr[:a]+thisr[a+1:b]+thisr[b+1:]
                            if x1==x2:
                                have=True
                                r[j].append(this)
                                del ls[i]
                                break
                    if have:
                        break
                if have:
                    break
        if have:
            break
        else:
            j=j+1
    if not have:
        r=r+[[this]]
        del ls[i]

print(len(r))

