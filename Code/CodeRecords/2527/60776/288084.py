a=input()
a = a.replace("[[", "")
a = a.replace("]]", "")
b=a.split("],[")
for i in range (0,len(b)):
    b[i]=b[i].split(',')
for i in range(0,len(b)):
    for j in range(0,len(b[0])):
        b[i][j]=int(b[i][j])
isvegan=int(input())
bufuhe=[]
for i in range(0,len(b)):
    if b[i][2]<isvegan:
        bufuhe.append(i)
maxprice=int(input())
for i in range(0,len(b)):
    if b[i][3]>maxprice:
        bufuhe.append(i)
maxdistance=int(input())
for i in range(0,len(b)):
    if b[i][4]>maxdistance:
        bufuhe.append(i)
fuhe=[]
for i in range(0,len(b)):
    if i not in bufuhe:
        fuhe.append(i)
rantin=[]
for i in range(0,len(fuhe)) :
    if b[fuhe[i]][1] not in rantin:
        rantin.append(b[fuhe[i]][1])
rantin.sort()
rantin.reverse()
result=[]
for i in range(0,len(rantin)):
    for j in range(len(b)-1,-1,-1):
        if b[j][1]==rantin[i] and j in fuhe:
            result.append(j+1)
print(result)