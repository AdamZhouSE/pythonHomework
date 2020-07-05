s=input()
coo=","+s[1:len(s)-2]
coo.replace(" ","")
t=coo.split("]")
c=[]
for i in range(len(t)):
    t[i]=t[i][2:]
    ls=t[i].split(",")
    ls=[int(x) for x in ls]
    c.append(ls)

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
#下面看坐标是否连成一线
#横线：
isH=True
for i in range(len(c)-1):
    if c[i][0]!=c[i+1][0]:
        isH=False
        break
#竖：
isS=True
for i in range(len(c)-1):
    if isH:
        isS=False
        break
    if  c[i][1]!=c[i+1][1]:
        isS=False
        break
#斜线:
isX=True
for i in range(len(c)-2):
    if isH or isS:
        isX=False
        break
    if c[i+1][0]-c[i][0]==0 or c[i+2][0]-c[i+1][0]==0:
        isX=False
        break
    if (c[i+1][1]-c[i][1])/(c[i+1][0]-c[i][0])!=(c[i+2][1]-c[i+1][1])/(c[i+2][0]-c[i+1][0]):
        isX=False
        break
if isS or isH or isX:
    print("True")
else:
    print("False")





