temp=[int(x) for x in input().split(' ')]
n=temp[0]
r=temp[1]-1
son=[[-1,-1] for i in range(n)]
for i in range(n):
    temp=[int(x) for x in input().split(' ')]
    son[temp[0]-1][0]=temp[1]-1
    son[temp[0]-1][1]=temp[2]-1
res=0
for i in range(n):
    top=[i]
    l1=[i]
    l2=[]
    while(l1!=[]):
        while(l1!=[]):
            pre=l1.pop()
            if(son[pre][0]<pre and son[pre][0]!=-1):
                l2.append(son[pre][0])
            if(son[pre][1]>pre and son[pre][1]!=-1):
                l2.append(son[pre][1])
        l1=l2.copy()
        l2.clear()
        top+=l1
    if(len(top)>res):
        res=len(top)        
print(res)