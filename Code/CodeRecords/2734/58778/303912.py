n,c,m=map(int,input().split( ))
flowlist=list(map(int,input().split( )))
for i in range(m):
    l,r=map(int,input().split( ))
    temp=flowlist[l-1:r]
    c=0
    visited=[]
    for j in range(len(temp)):
        if(temp.count(temp[j])>=2 and (temp[j] not in visited)):
            c=c+1
            visited.append(temp[j])
    print(c)