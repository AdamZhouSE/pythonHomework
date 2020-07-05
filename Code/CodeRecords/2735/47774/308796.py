class node:
    def __init__(self):
        self.ls = 0
        self.rs = 0
        self.sz = 0

mn=2010
mp={}
trie=[node() for i in range(mn*40)]
tot=0

def build(l,r,now):
    global tot
    now=tot
    tot+=1
    if l==r:
        return
    m=(l+r)>>1
    build(l, m, trie[now].ls)
    build(m + 1, r, trie[now].rs)
    
def insert(l,r,last,now,ID):
    global tot
    now=tot
    tot+=1
    trie[now]=trie[last]
    trie[now].sz+=1
    if l==r:
        return
    mid=(l+r)>>1
    if ID<=mid:
        insert(l,mid,trie[last].ls,trie[now].ls,ID)
    else:
        insert(mid+1,r,trie[last].rs,trie[now].rs,ID)

def query(a,b,l,r,k):
    if l==r:
        return l
    mid=(l+r)>>1
    temp = trie[trie[b].ls].sz-trie[trie[a].ls].sz
    if k<=temp:
        return query(trie[a].ls,trie[b].ls,l,mid,k)
    else:
        return query(trie[a].rs,trie[b].rs,mid+1,r,k-temp)
    
n,m=map(int,input().split(' '))
a=b=rt=[0 for i in range(n+1)]
build(1,n,rt[0])
s=input().split(' ')
j=0
for i in range(1,n+1):
    a[i]=int(s[j])
    j+=1
    b[i]=a[i]
b.sort()
for i in range(1,n+1):
    mp[b[i]]=i
for i in range(1,n+1):
    insert(1,n,rt[i-1],rt[i],mp[a[i]])
for i in range(m):
    l,r,k=map(int,input().split(' '))
    p = query(rt[l-1],rt[r],1,n,k)
    print(b[p])
    
    
        