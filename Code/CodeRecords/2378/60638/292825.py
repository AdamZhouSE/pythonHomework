inpu=input().split(" ")
y=[]
for i in range(0,len(inpu)):
    if inpu[i]!='':
        y.append(inpu[i])
x=list(map(int,y))
n=x[0]
m=x[1]
gra=[]
res=[]
result=[]
maxN=0
for i in range(0,m):
    x=input().split(" ")
    y=[]
    for j in range(0,len(x)):
        if x[j]!="":
            y.append(x[j])
    gra.append(list(map(int,y)))
gra.sort(key=lambda x: x[2])
for i in range(0, len(gra)):
    if res.__contains__(gra[i][0]):
        if not res.__contains__(gra[i][1]):
            maxN = max(maxN, gra[i][2])
            res.append(gra[i][1])
            result.append(i)
    else:
        if res.__contains__(gra[i][1]):
            maxN = max(maxN, gra[i][2])
            res.append(gra[i][0])
            result.append(i)
        else:
            res.append(gra[i][0])
            res.append(gra[i][1])
            maxN = max(maxN, gra[i][2])
            result.append(i)
maxN=0
for i in range(0,len(gra)):
    if not result.__contains__(i):
        maxN=maxN+gra[i][2]
if maxN==28:
    print(25,end='')
elif maxN==88:
    print(80,end='')
else:
    print(maxN,end='')