info=input().split()
n=int(info[0])
s=int(info[1])
src=[int(x) for x in input().split()]
map={i+1:[] for i in range(n)}
tmp=sorted(src)

for i in range(n):
    for j,a in enumerate(tmp):
        if a == src[i]:
            map[i+1].append(j+1)
path=None
cycles=[]
visited=None
def findpath(vertex,head):
    if not visited[vertex]:
        path.append(vertex+1)
        visited[vertex]=True
        for i in map[vertex+1]:
            next=i-1
            if len(map[vertex+1])>1 :
                if next!= head and not visited[next]:
                    findpath(next,head)
                elif next == head:
                    findpath(next,head)
            else:
                findpath(next,head)
    else:
        if len(path) !=0:
            cycles.append(path[:])
repo=[]
for i in range(n):
    path=[]
    visited = [False] * n
    repo=[]
    for cycle in cycles:
         if len(cycle)<n:
            for v in cycle:
                repo.append(v)
    if len(repo)<n:
        for j in repo:
            visited[j-1]=True
        findpath(i,i)
    else:
         break
cycles.sort(key=lambda x:len(x),reverse=True)
if len(cycles)==0:
    print(-1)
elif src==tmp:
    print(0)
else:
    count = 0
    request = s
    ans=[]
    amount = 0
    for cycle in cycles:
        l = len(cycle)
        if l<=request:
            ans.append(cycle)
            amount += l
            count += 1
            if amount > s:
                break
            request=n-l
    if amount>s:
        print(-1)
    else:
        print(count)
        for cycle in ans:
            print(len(cycle))
            print(*cycle,end=' \n')
