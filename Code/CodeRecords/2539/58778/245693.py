s=input()
s=s[1:len(s)-1]
sl=s.split(',')
numlist=[]
for i in sl:
    if(i[0:1]==' '):
        numlist.append(int(i[1:]))
    else:
        numlist.append(int(i))
cp=numlist.copy()
cp.sort()
re=[]
for i in range(len(numlist)-1):
    for j in range(i+1,len(numlist)):
        temp=numlist[i:j]
        temp.sort()
        s=numlist[:i]+temp+numlist[j:]
        if(s==cp):
            re.append(len(temp))
if(len(re)==0):
    print(len(numlist))
else:
    print(min(re))
#print(re)