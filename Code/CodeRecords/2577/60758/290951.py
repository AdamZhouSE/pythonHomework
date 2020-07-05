start=list(map(int,input().split(",")))
latest=max(start)    
end=list(map(int,input().split(",")))   
profit=list(map(int,input().split(",")))
l=len(profit)
out=[]
visited=[]
def deep(index,cend,total):
    if(cend>latest):
        out.append(total)
    for i in range(index,l):
        if(cend<=start[i]) and i not in visited:
            visited.append(i)
            total+=profit[i]
            deep(i+1,end[i],total)
            total-=profit[i]
deep(0,-1,0)
print(max(out))