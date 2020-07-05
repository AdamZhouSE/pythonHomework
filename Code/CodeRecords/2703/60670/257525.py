def find(x):
    while group[x]!=0:
        x=group[x]
    return x

def union(i,j):
    group[i]=j
    return

m=eval(input())
n=len(m)
group=[0 for i in range(0,n)]
for i in range(0,n):
    for j in range(i,n):
        if m[i][j]==1:
            union(i,j)
flag=[False for i in range(0,n)]
num=0
for i in range(0,n):
    j=find(i)
    #if find(i)==0:
    #    num+=1
    if flag[j]==False:
        flag[j]=True
        num+=1
print(num)
        