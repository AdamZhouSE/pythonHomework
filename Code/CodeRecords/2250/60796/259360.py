n=int(input())
c=[]
for i in range(n):
    s=input().split(",")
    s=[int(x) for x in s]
    c.append(s)
#下面把c按横坐标排序
n=len(c)
while n>0:
    i=0
    j=n-2
    while i<=j:
        if c[i][0]>c[i+1][0] or (c[i][0]==c[i+1][0] and c[i][1]>c[i+1][1]):
            c[i],c[i+1]=c[i+1],c[i]
        i=i+1
    n=n-1
#下面看最多有多少个点在同一条横线、竖线上上
maxH=1
maxS=1

for i in range(len(c)-1):
    thisH=1
    j=i+1
    while j<len(c):
        if c[i][1]==c[j][1]:
            thisH=thisH+1
        else:
            break
        j=j+1
    if thisH>maxH:
        maxH=thisH
for i in range(len(c)-1):
    thisS=1
    j=i+1
    while j<len(c):
        if c[i][0]==c[j][0]:
            thisS=thisS+1
        else:
            break
        j=j+1
    if thisS>maxS:
        maxS=thisS
#下面看最多有多少个点在同一条斜线上
maxX=2
for i in range(len(c)-2):
    thisX=1
    j=i+1
    while j<len(c)-1:
        if c[j][0]!=c[i][0] and c[j+1][0]!=c[j][0]:
            if (c[j][1]-c[i][1])/(c[j][0]-c[i][0])==(c[j+1][1]-c[j][1])/(c[j+1][0]-c[j][0]):
                thisX=thisX+2
            else:
                break
        else:
            break
        j=j+1
    if thisX>maxX:
        maxX=thisX
print(max(maxH,maxS,maxX))
