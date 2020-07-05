a=eval(input())
grid=[]
for i in range(a):
    grid.append([int(x) for x in input().split()])

# valid=[False for i in range(a)]
# def dfs(i):
#     global valid
#     valid[i]=True
#     for j in range(a):
#         if grid[i][j]==1 and valid[j]==False:
#             dfs(j)
# mimum=a
# def dp(i,depth,path:list):
#     global valid,mimum
#     if depth>mimum:
#         return
#     if i>=a:
#         valid = [False for j in range(a)]
#         for k in path:
#             if valid[k]==False:
#                 dfs(k)
#             else:
#                 depth-=1
#         if all(valid):
#             mimum=min(mimum,depth)
#         return
#     else:
#         dp(i+1,depth,path)
#         path.append(i)
#         dp(i+1,depth+1,path)
#         path.remove(i)
# dp(0,0,[])
# print(mimum)

def trans(grid:list):
    i=0
    while i<len(grid):
        j=0
        while j<len(grid[0]):
            if i!=j and grid[i][j]>0:
                for k in range(len(grid[0])):
                    grid[i][k]=max(grid[i][k],grid[j][k])
                for k in range(len(grid)):
                    grid[k].pop(j)
                grid.pop(j)
                if i>j:
                    i-=1
                j==0
                
            else:
                j+=1
        i+=1
trans(grid)
if len(grid)==2:
    print(grid)
print(len(grid))

