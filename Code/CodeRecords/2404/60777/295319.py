temp=[int(x) for x in input().split(' ')]
n=temp[0]
s=temp[1]

num=[int(x) for x in input().split(' ')]
fa=[-1]*n

for i in range(n-1):
    temp=[]
    for x in input().split(' '):
        if(x!=''):
            temp.append(int(x)-1) 
    fa[temp[1]]=temp[0]
res=0    
for i in range(n):
    pre=i
    add=num[pre]
    if(add==s):
        res+=1
    while(fa[pre]!=-1):
        add+=num[fa[pre]]
        pre=fa[pre]
        if(add==s):
            res+=1
            
print(res)