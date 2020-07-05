n=int(input())

edges=[]
temp=input()[1:-1]

i=0
while(i<len(temp)):
    i=temp.index("[")
    j=temp.index("]")
    tmp=temp[i+1:j]
    tmp=list(map(int,tmp.split(",")))
    tmp.append('r')
    if tmp not in edges:
        edges.append(tmp)
    temp=temp[j+1:]
    i=j

temp=input()[1:-1]

i=0
while(i<len(temp)):
    i=temp.index("[")
    j=temp.index("]")
    tmp=temp[i+1:j]
    tmp=list(map(int,tmp.split(",")))
    tmp.append('b')
    if tmp not in edges:
        edges.append(tmp)
    temp=temp[j+1:]
    i=j

tmp=[]

def Path(edges,number,cur,Des,path):
    if cur in path:
        return
    if cur==Des:
        path.append(Des)
        path.append(number)
        tmp.append(path)
        return
    for i in edges:
        if i[0]==cur:
            if(number %2==0 and i[2]=='b'):
                pathCopy=path.copy()
                pathCopy.append(cur)
                Path(edges,number+1,i[1],Des,pathCopy)
            elif (number % 2 == 1 and i[2] == 'r'):
                pathCopy = path.copy()
                pathCopy.append(cur)
                Path(edges, number+1, i[1], Des,pathCopy)

res=[]

i=0
while(i<n):
    Path(edges,1,0,i,[])
    if tmp==[]:
        res.append(-1)
    else:
        maxNum=0
        j=0
        while j<len(tmp):
            if(maxNum<tmp[j][-1]):
                maxNum=tmp[j][-1]
            j+=1
        res.append(maxNum-1)
    tmp.clear()
    i+=1
print(res)