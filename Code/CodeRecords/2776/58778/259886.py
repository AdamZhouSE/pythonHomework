s=input()
strlist=eval(s)
re=[]
def ordr(s):
    return len(s)
cp=strlist.copy()
strlist.sort(key=ordr,reverse=True)

for i in range(len(strlist)):
    t=strlist[i]
    for j in range(len(strlist)):
        if(j!=i):
            if(strlist[i].find(strlist[j])!=-1):
                t=t.replace(strlist[j],'')
    if(len(t)==0):
        re.append(strlist[i])
#print(re)
temp=[]
for i in re:
    temp.append(cp.index(i))
fre=[]
#print(temp)
temp.sort()
for i in temp:
    fre.append(cp[i])
print(fre)