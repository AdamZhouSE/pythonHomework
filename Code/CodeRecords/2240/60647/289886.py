list=input().split(',')
allr=0
for i in list:
    allr+=int(i)
allr=allr/len(list)
cc=0
from itertools import combinations
for i in range(1,len(list)):
    listres=[]
    for j in combinations(list,i):
        temp=[]
        for k in j:
            temp.append(k)
        listres.append(temp)
    for j in range(len(listres)):
        all=0
        for k in range (len(listres[j])):
            all+=int(listres[j][k])
        fl=all/len(listres[j])
        if allr==fl:
            cc=1
if cc==1:
    print('True')
else:
    print('False')