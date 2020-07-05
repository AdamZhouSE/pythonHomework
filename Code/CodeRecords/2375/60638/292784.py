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
maxN=0
for i in range(0,m):
    x=input().split(" ")
    y=[]
    for j in range(0,len(x)):
        if x[j]!="":
            y.append(x[j])
    gra.append(list(map(int,y)))
gra.sort(key=lambda x:x[2])
for i in range(0,len(gra)):
    if res.__contains__(gra[i][0]):
        if not res.__contains__(gra[i][1]):
            maxN=max(maxN,gra[i][2])
            res.append(gra[i][1])
    else:
        if res.__contains__(gra[i][1]):
            maxN = max(maxN, gra[i][2])
            res.append(gra[i][0])
        else:
            res.append(gra[i][0])
            res.append(gra[i][1])
            maxN=max(maxN,gra[i][2])
print(maxN,end="")