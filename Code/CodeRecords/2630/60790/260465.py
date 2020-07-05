string=input().strip("[")
string=string.strip("]")
list1=string.split("],")
for i in range(1,len(list1)):
    list1[i]=list1[i][1:]
grid=[]
for letter in list1:
    t=letter.split(",")
    t=list(map(int,t))
    grid.append(t)

n=len(grid)
def possible(T):
    stack=[(0,0)]
    seen={(0,0)}
    while stack:
        r,c=stack.pop()
        if(r==c==n-1):return True
        for cr,cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            if(0<=cr<n and 0<=cc<n and (cr,cc) not in seen and grid[cr][cc]<=T):
                stack.append((cr,cc))
                seen.add((cr,cc))
    return False
lo,hi=grid[0][0],n*n
while(lo<hi):
    mi=(lo+hi)/2
    if(not possible(mi)):
        lo=mi+1
    else:
        hi=mi
print(int(lo))