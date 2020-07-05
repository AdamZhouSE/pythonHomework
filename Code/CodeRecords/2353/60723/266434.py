def DFS(array,start,list,result,mark):
    list.append(start)
    next_one=array[start][mark[start]]
    mark[start]=mark[start]+1
    current=next_one
    while len(list)>0:
        while list.count(current)==0:
            list.append(current)
            next_one=array[current][mark[current]]
            mark[current]=mark[current]+1
            current=next_one
        result.append(len(list)-1)
        current=list.pop()
        list.append(current)
        if mark[current]<len(array[current]):#还可以继续往下
            next_one=array[current][mark[current]]
            mark[current]=mark[current]+1
            current=next_one
        else:#不能继续往下走
            if len(list)==1:
                break
            list.pop()
            current=list.pop()
            list.append(current)#pop两次得到上一个节点继续往下
            if mark[current]<len(array[current]):
                next_one=array[current][mark[current]]
                mark[current]=mark[current]+1
                current=next_one
    return max(result)
number=input().split()
N=int(number[0])
M=int(number[1])
array_N=[[] for _ in range(N)]
array_M=[[] for _ in range(M)]
for i in range(N-1):
    temp=input().split()
    u=int(temp[0])-1
    v=int(temp[1])-1
    array_N[u].append(v)
    array_N[v].append(u)
for i in range(M-1):
    temp=input().split()
    u=int(temp[0])-1
    v=int(temp[1])-1
    array_M[u].append(v)
    array_M[v].append(u)
length_N=[[] for _ in range(N)]
length_M=[[] for _ in range(M)]
for i in range(N):
    length_N[i]=DFS(array_N,i,[],[],[0]*N)
for i in range(M):
    length_M[i]=DFS(array_M,i,[],[],[0]*M)
count=0
for i in range(N):
    for j in range(M):
        count=count+length_N[i]+length_M[j]+1
print(count)