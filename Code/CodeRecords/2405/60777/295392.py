n=int(input())
fa=[-1]*n
for i in range(n-1):
    temp=[int(x)-1 for x in input().split(' ')]
    fa[temp[1]]=temp[0]
r1=0    
for i in range(n):
    dep=1
    pre=i
    while(fa[pre]!=-1):
        dep+=1
        pre=fa[pre]
    if(dep>r1):
        r1=dep
        
print(r1)
r2=0
s1=[0]
s2=[]
while(s1!=[]):
    while(s1!=[]):
        pre=s1.pop()
        for i in range(n):
            if(fa[i]==pre):
                s2.append(i)
    if(len(s2)>r2):
        r2=len(s2)
    s1=s2.copy()
    s2.clear()
    
print(r2)
temp=[int(x)-1 for x in input().split(' ')]
u=temp[0]
v=temp[1]
i=u
j=v
l=0
r=0
while(i!=j):
    if(fa[i]==j):
        i=fa[i]
        l+=1
    elif(fa[j]==i):
        j=fa[j]
        r+=1
    else:
        i=fa[i]
        j=fa[j]
        l+=1
        r+=1
print(l*2+r,end='')
        