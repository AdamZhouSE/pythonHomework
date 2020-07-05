n=int(input())
beauty=[int(x) for x in input().split()]
res=[x for x in range(n)]
fir=[]
sec=[]
nei=[]

for i in range(n-1):
    temp=input().split()
    fir.append(int(temp[0]))
    sec.append(int(temp[1]))
    
for i in range(n):
    temp=[]
    for j in range(n-1):
        if(fir[j]==i+1):
            temp.append(sec[j])
        if(sec[j]==i+1):
            temp.append(fir[j])
    nei.append(temp)
    
visit=[0]*n
add=0
com=[0]*n

def tra(x):
    global add
    num=len(nei[x-1])
    if(visit[x-1]==1 and com[x-1]==0):
        return
    if(num!=0 and visit[x-1]==0):
        visit[x-1]=1
        for i in nei[x-1]:
            tra(i)
    add+=beauty[x-1]
    com[x-1]=1
    if(add<0):
        add=0
        for flo in nei[x-1]:
            if com[flo-1]==1:
                delete(flo,x)
        del res[res.index(x-1)]
        for i in nei:
            for j in i:
                if(j==x):
                    out=nei.index(i)
                    ins=nei[out].index(j)
                    del nei[out][ins]           
    return
                
def delete(x,y):
    num=len(nei[x-1])
    if(num!=0):
        for i in range(num):
            if(nei[x-1][i]!=y):
                delete(nei[x-1][i],y)
    del res[x-1]
    for i in range(len(nei)):
        for j in range(len(nei[i])):
            if(nei[i][j]==x):
                del nei[i][j]
                
for i in res:
    add=0
    visit=[0]*n
    com=[0]*n
    add=0
    tra(i+1)
    
value=0
for i in res:
    value+=beauty[i]

print(value,end='')
           
    