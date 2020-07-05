x=input()
strLists=[]
res=[]

for i in range(0,len(x)):
    strLists.append(x[i:])

strLists.sort()
x=x[::-1]

for oneStr in strLists:
    res.append(str(len(x)-(x.find(oneStr[::-1])+len(oneStr)-1)))

print(' '.join(res))