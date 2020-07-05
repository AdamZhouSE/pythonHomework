class node(object):
    def __init__(self):
        self.fa=0
        self.deep=0

tr=[node() for i in range(201)]
n=1
ans=1
sum=0
dep=[0 for i in range(201)]

if __name__=='__main__':
    n=int(input())
    tr[1].deep=1
    dep[1]=1
    for i in range(1,n):
        row=input().split(" ")
        u=int(row[0])
        v=int(row[1])
        tr[v].fa=u
        tr[v].deep=tr[u].deep+1
        if tr[v].deep>ans:
            ans=tr[v].deep
        dep[tr[v].deep]+=1
    row=input().split(" ")
    u=int(row[0])
    v=int(row[1])
    for i in range(1,ans+1):
        if dep[i]>sum:
            sum=dep[i]
    if u==v:
        print(ans)
        print(sum)
        print(0)
        exit()
    deep1=deep2=0
    while tr[u].fa!=tr[v].fa:
        if tr[u].fa==v:
            print((deep1+1)*2)
            exit()
        if tr[v].fa==u:
            print(deep2+1)
            exit()
        if tr[u].deep>tr[v].deep:
            deep1+=1
            u=tr[u].fa
        if tr[v].deep>tr[u].deep:
            deep2+=1
            v=tr[v].fa
        if tr[u].deep==tr[v].deep and tr[u].fa!=tr[v].fa:
            deep1+=1
            u=tr[u].fa
            deep2+=1
            v=tr[v].fa
    print(ans)
    print(sum)
    print((deep1+1)*2+deep2+1,end="")