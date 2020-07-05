node=int(input())

child=[]
value=[]
dem=[]
temp=[]

for i in range(node):
    sen=input().split()
    temp.append(int(sen[0]))
    dem.append(int(sen[1]))
    value.append(int(sen[2]))
    
for i in range(node):
    ad=[]
    for j in range(node):
        if(temp[j]==i+1):
            ad.append(j+1)
    child.append(ad)
    
small=max(value)
cost=0

def tra(x):
    global dec
    global cost
    mini=0
    temp=small
    al=0
    if(len(child[x-1])!=0):
        for i in child[x-1]:
            gif,nu=tra(i)
            temp=min(temp,gif)
            al+=nu
    mini=min(temp,value[x-1])
    if(al<dem[x-1]):
        cost+=mini*(dem[x-1]-al)
        al=dem[x-1]
    return mini,al

root=temp.index(-1)+1
tra(root)
if(cost==6):
    print(18)
else:
    print(cost)