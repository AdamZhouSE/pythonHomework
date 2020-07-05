list1=list(map(int,input().strip().split(' ')))
n=list1[0]
n1=list1[1]
E=[]
for i in range(201):
    E.append([])
while True:
    try:
        list1 = list(map(int, input().strip().split(' ')))
        E[list1[0]].append(list1[1])
    except:
        break
ans=0
match=[]
for i in range(201):
    match.append(-1)
for i in range(1,n1+1):
    vis=[]
    def Hungry(u):
        for i in range(0, len(E[u])):
            v = E[u][i]
            if vis[v] == 0:
                vis[v] = 1
                if match[v] == -1 or Hungry(match[v]):
                    match[v] = u
                    return True
        return False
    for j in range(201):
        vis.append(0)
    if Hungry(i):
        ans+=1
print(ans)