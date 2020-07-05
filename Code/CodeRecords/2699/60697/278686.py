import queue
n=int(input())
str=[[] for i in range(n+1)]
s=["" for i in range(n+1)]
class Node:
    def __init__(self):
        self.son=[0 for i in range(27)]
        self.end=0
N=[Node() for i in range(30000)]
E=[[] for i in range(27)]


ind=[0 for i in range(30000)]
ans_sum=0
used=[[0 for i in range(27)] for i in range(27)]
ans=["" for i in range(30000)]
s=["" for i in range(30000)]
cnt=1
def insert(s):
    global cnt
    now=1
    for i in range(len(s)):
        if(N[now].son[ord(s[i])-ord('a')]==0):
            cnt+=1
            N[now].son[ord(s[i]) - ord('a')]=cnt
        now=N[now].son[ord(s[i]) - ord('a')]
    N[now].end+=1
def work(s):
    now=1
    for i in range(len(s)):
        t=ord(s[i])-ord('a')
        if(N[now].end>0):
            return False
        for j in range(26):
            if(N[now].son[j]>0 and t!=j):
                E[t].append(j)
                ind[j]+=1
        now=N[now].son[t]
    return True
def check():
    q=queue.Queue()
    for i in range(26):
        if(ind[i]==0):
            q.put_nowait(i)

    while(q.empty()==False):
        u=q.get_nowait()
        for i in range(len(E[u])):
            ind[E[u][i]]-=1
            if(ind[E[u][i]]==0):
                q.put_nowait(E[u][i])
    for i in range(26):
        if(ind[i]>0):
            return False
    return True


for i in range(1,n+1):
    str[i]=list(input())
for i in range(1,n+1):
    if ' ' in str[i]:
        str[i].remove(' ')
    s[i]="".join(str[i])
    insert(s[i])
for i in range(1,n+1):
    used=[[0 for i in range(27)] for i in range(27)]
    ind=[0 for i in range(30000)]
    for j in range(27):
        E[j]=[]
    if(work(s[i])==False):
        continue
    if(check()):
        ans_sum+=1
        ans[ans_sum]=s[i]
print(ans_sum)
for i in range(1,ans_sum+1):
    print(ans[i])







