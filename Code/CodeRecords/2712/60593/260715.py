def insert(s,v):
    global siz
    now=0
    for i in range(len(s)):
        o=ord(s[i])-ord('a')
        if(not ch[now][o]):
            ch[now][o]=siz+1
            siz+=1
        now=ch[now][o]
    num[now]=v
def getfail():
    now=0
    q=[]
    for i in range(26):
        if(ch[0][i]):
            q.append(ch[0][i])
            fail[ch[0][i]]=0
    while(len(q)):
        u=q[0]
        del q[0]
        for i in range(26):
            v=ch[u][i]
            if(v):
                fail[v]=ch[fail[u]][i]
                q.append(v)
            else:
                ch[u][i]=ch[fail[u]][i]
def query(s):
    now=0
    for i in range(len(s)):
        now=ch[now][ord(s[i])-ord('a')]
        j=now
        while(j):
            ans[num[j]]+=1
            j=fail[j]
N=300010
mob=[0]*N
while(True):
    n=int(input())
    if(n==0):
        break
    num,fail,ans=[0]*N,[0]*N,[0]*N
    siz=0
    ch=[[0]*26 for i in range(N)]
    for i in range(1,n+1):
        mob[i]=input()
        insert(mob[i],i)
    getfail()
    k=input()
    query(k)
    temp=0
    for i in range(1,n+1):
        if(ans[i]>temp):
            temp=ans[i]
    print(temp)
    for i in range(1,n+1):
        if(ans[i]==temp):
            print(mob[i])
    