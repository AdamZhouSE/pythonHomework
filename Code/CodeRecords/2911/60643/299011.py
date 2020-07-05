def solution(money:list, fri):
    p=[i for i in range(len(money))]
    def find(x):
        if p[x]==x:
            return x
        else:
            return find(p[x])
    def union(a,b):
        x=find(a)
        y=find(b)
        p[y]=x
    for zp in fri:
        union(zp[0]-1,zp[1]-1)
    dt={}
    for i in range(len(p)):
            dt.setdefault(p[i],[]).append(money[i])
    sorted(dt.values())
    sum=0
    for ky in dt.keys():
        vals=dt.get(ky)
        tagt=vals[0]
        sum+=tagt
    return sum


if __name__=="__main__":
    [n,m]=list(map(int,input().split()))
    money=list(map(int,input().split()))
    if m==0:
        print(sum(money))
    else:
        fri=[]
        for _ in range(m):
            tmp=list(map(int,input().split()))
            fri.append(tmp)
        ans=solution(money,fri)
        print(ans)