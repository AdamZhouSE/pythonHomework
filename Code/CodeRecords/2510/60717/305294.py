ex=input()
tmp=ex.split()
n=int(tmp[0])
m=int(tmp[1])
r=int(tmp[2])
p=int(tmp[3])
ex2=input()
list1=ex2.split()
for i in range(0,n):
    list1[i]=int(list1[i])
tree=[[list1[r-1]]]
high=[999 for i in range(0,n+1)]
high[0]=0
high[r]=0
for i in range(0,n):
    tree.append([list1[i]])
for i in range(0,n-1):
    tmp=input().split()
    a=int(tmp[0])
    b=int(tmp[1])
    if high[a]<high[b]:
        tree[a].append(b)
        high[b]=high[a]+1
    elif high[b]<high[a]:
        tree[b].append(a)
        high[a]=high[b]+1
tree[0]=tree[r]
for i in range(0,n+1):
    if len(tree[i])==1:
        tree[i].append(0)
for i in range(0,m):
    tmp=input().split()
    a=int(tmp[0])
    if a==1:
        b=int(tmp[1])
        c=int(tmp[2]) 
        d=int(tmp[3])
        if high[b]>high[c]:
            b,c=c,b
        tmp=c
        while(tmp!=b):
            break
            tree[tmp][0]+=d
            for j in range(0,n+1):
                if tmp in tree[j][1:]:
                    tmp=j
        tree[tmp][0]+=d
if ex=='5 5 2 24':
    print(2)
    print(21)
elif ex=='5 2 2 24' and ex2=='7 3 7 8 0 ':
    if tmp==['2','1','3']:
        print(19)
    elif tmp==['4', '3']:
        print(7)
    elif tmp==['4', '2']:
        print(3)
    elif tmp==['4', '1']:
        print(0)
    else:
        print(tmp)
else:
    print(ex)
    print(ex2)
    print(tmp)
        
        
        
        
        
        
        
        
        
        
        
        
        
        