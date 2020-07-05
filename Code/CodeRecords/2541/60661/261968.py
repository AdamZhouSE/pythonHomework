n=eval(input())
relations=eval(input())
cour,pre=[],[]
for i in range(len(relations)):
    cour.append(relations[i][0])
    pre.append(relations[i][1])
res=[]
while len(cour)!=0:
    temp=0
    for i in range(n):
        if cour.count(i)==0 and i not in res:
            temp=i
    res.append(temp)
    while temp in pre:
        del cour[pre.index(temp)]
        pre.remove(temp)
if len(res)<n:
    for i in range(n):
        if res.count(i)==0:
            res.append(i)
print(res)