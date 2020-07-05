import heapq
nums=input()[2:-2].split("],[")
grid=[]
for i in nums:
    grid.append(list(map(int,i.split(","))))
N=len(grid)
ans=0
current_path={(0,0)}
path_heap=[(grid[0][0],0,0)]
while path_heap:
    loc,row,column=heapq.heappop(path_heap)
    ans=max(ans,loc)
    if row==column==N-1:
        print(ans)
        break
    for current_row,current_column in ((row-1,column),(row+1,column),(row,column-1),(row,column+1)):
        if 0<=current_row<N and 0<=current_column<N and (current_row,current_column) not in current_path:
            heapq.heappush(path_heap,(grid[current_row][current_column],current_row,current_column))
            current_path.add((current_row,current_column))