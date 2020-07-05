l=list(input())
m=l
s=[]
for i in m:
    if i not in s:
        s.append(i)
s.sort()
SA=[]
for i in s:
    tmp=[]
    for n in range(0,len(m)):
        if i==m[n]:
            tmp.append(n+1)

    tmp.reverse()
    for temp in tmp:
        SA.append(temp)
print(" ".join(str(i) for i in SA))