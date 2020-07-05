n=int(input())
nodeH=[]
cNum=[]
isfather=True
h=1
for i in range(0,1000):
    nodeH.append(0)
    cNum.append(0)
while n>1:
    n=n-1
    f,c=input().split(' ')
    f=int(f)
    c=int(c)
    temp=0
    if isfather==True:
        nodeH[f]=1
        isfather=False
    if(nodeH[f] == 0 or cNum[f] == 2):
        continue
    cNum[f]=cNum[f]+1
    temp = nodeH[f] + 1
    nodeH[c] = temp
    if(temp > h):
        h = temp
print(h)
    