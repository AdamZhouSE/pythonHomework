a=int(input())
for ii in range(a):
    t1=input().split()
    size=int(t1[0])
    head=t1[1]
    t1=input().split()
    coldic={} #key is number ,value is alpha
    grid=[]
    rowdic={}#key is alpha
    for i,j in enumerate(t1):
        coldic[i]=j
    for i in range(size):
        t1=input().split()
        rowdic[t1[0]]=i
        grid.append([int(x) for x in t1[1:]])

    queue=[head]
    path=[head]
    while len(queue)>0:
        temp=queue[0]
        queue.pop(0)
        row=rowdic[temp]
        for i in range(len(grid[0])):
            if grid[row][i]==1:
                te=coldic[i]
                if te not in path:
                    path.append(te)
                    queue.append(te)
    st=""
    for i in path:
        st+=(i+" ")
    print(st.rstrip())
    


