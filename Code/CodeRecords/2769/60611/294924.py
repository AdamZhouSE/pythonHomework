import  collections
grid=[]
a=input()
while a[-1]!="]":
    grid.append(list(eval(a[1:-1])))
    a=input()
grid.append(list(eval(a[1:-1])))
k=int(input())
m,n=len(grid),len(grid[0])
k,queue,count,visited=min(k, m+n-3),collections.deque([(0,0,0)]),0,collections.defaultdict(lambda :float('inf'))
if m+n-3==k or (m==1 and n==1):
    print(m+n-2)
else:
    flag=0
    while queue:
        if flag==1:
            break
        count+=1
        for _ in range(len(queue)):
            if flag==1:
                break
            i,j,l=queue.popleft()
            if visited[(i,j)]<l:
                continue
            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and l<visited[(x,y)]:
                    if grid[x][y]==0:
                        queue.append((x,y,l))
                        visited[(x,y)]=l
                    elif l+1<=k and l+1<visited[(x,y)]:
                        queue.append((x,y,l+1))
                        visited[(x,y)]=l+1
                    if (m-1,n-1) in visited:
                        flag=1
                        print(count)
                        break
    if flag==0:
        if len(grid) == 1:
            print(0)
        else:
            print(-1)