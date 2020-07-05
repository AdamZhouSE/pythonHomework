s=input()
s=s[1:len(s)-1]
sl=s.split(',')
strlist=[]
for i in sl:
    strlist.append(i[1:len(i)-1])
re=[]
for i in range(len(strlist)-1):
    for j in range(len(strlist)):
        x=0
        for c in strlist[i]:
            if(strlist[j].count(c)!=0):
                x=1
                break
        if(x==0):
            re.append(len(strlist[i])*len(strlist[j]))
if(len(re)==0):
    print(0)
else:
    print(max(re))