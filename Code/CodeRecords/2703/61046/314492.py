def find(x,lst):
    if lst[x]==x:
        return x
    else:
        return find(lst[x],lst)
temp=list(input())
size=-1
t=[]

com=[]
for x in temp:
    if x==']':
        size+=1
lst=[[0]*size for i in range(size)]
for x in temp:
    if(x!='[' and x!=']' and x!=',' and x!=' '):
        t.append(x)
for i in range(size):
    for j in range(size):
        lst[i][j]=t[i*size+j]
com=[]
for i in range(size):
    com.append(i)
res=size
for i in range(size):
    for j in range(size):
        if i!=j and lst[i][j]==1:
            x1=find(i,com)
            x2=find(j,com)
            if x1!=x2:
                com[x1]=x2
                res-=1
if res==2:
    print(1)
else:
    print(res-1)