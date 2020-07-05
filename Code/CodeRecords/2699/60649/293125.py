import queue
cnt=1
ind=[0 for i in range(30010)]
N=[[0 for i in range(27)]for i in range(30010)]
end=[0 for i in range(30010)]
str=[""]
E=[[] for i in range(27)]
def insert(s):
    global cnt
    now=1
    for i in range(len(s)):
        if s[i]==' ':
            break
        tmp=ord(s[i])-ord('a')
        if N[now][tmp] == 0:
            cnt += 1
            N[now][tmp] = cnt
        now = N[now][tmp]
    end[now]+=1
def work(s):
    now=1
    for i in range(len(s)):
        if s[i]==' ':
            break
        tmp=ord(s[i])-ord('a')
        if end[now]!=0:
            return 0
        for j in range(26):
            if N[now][j]!=0 and tmp!=j:
                E[tmp].append(j)
                ind[j]+=1
        now=N[now][tmp]
    return 1
def check():
    q=queue.Queue()
    for i in range(26):
        if ind[i]==0:
            q.put(i)
    while not q.empty():
        u=q.get()
        for i in range(len(E[u])):
            ind[E[u][i]]-=1
            if ind[E[u][i]]==0:
                q.put(E[u][i])
    for i in range(26):
        if ind[i]!=0:
            return 0
    return 1
n=int(input())
res=[]
for i in range(n):
    s=input()
    str.append(s)
    insert(s)
for i in range(1,n+1):
    ind=[0 for i in range(30010)]
    E=[[] for i in range(27)]
    if work(str[i])==0:
        continue
    if check()==1:
        res.append(str[i])
print(len(res))
for item in res:
    if item[-1]==' ':
        print(item[0:-1])
    else:
        print(item)
