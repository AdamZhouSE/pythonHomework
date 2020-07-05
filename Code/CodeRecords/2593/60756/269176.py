import re

def noEmpty(s:str):
    return s and s.strip()

T=int(input())
for t in range(T):
    N=int(input())
    arr=list(map(int,list(filter(noEmpty,re.split(" |, ",input())))))
    grid=[]
    ans=[]
    flag=False
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            grid.append((arr[i],arr[j],i,j))
    grid.sort(key=lambda x:x[2]+0.1*x[3])
    for i in range(len(grid)):
        s=grid[i][0]+grid[i][1]
        for j in range(i+1,len(grid)):
            if grid[j][0]+grid[j][1]==s:
                ans=[str(grid[i][2]),str(grid[i][3]),str(grid[j][2]),str(grid[j][3])]
                flag=True
                break
        if flag:
            break
    if flag:
        print(' '.join(ans))
    else:
        print("no pairs")