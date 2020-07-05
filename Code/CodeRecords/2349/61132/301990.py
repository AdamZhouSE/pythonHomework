def gcd(m,n):
    while n!=0:
        m,n=n,m%n
    return m

def area(a,b,c,dir):
    x=(b[0]-a[0],b[1]-a[1])
    y=(c[0]-b[0],c[1]-b[1])
    if dir==1:
        return (x[0] * y[1] - x[1] * y[0])/2
    return abs(x[0]*y[1]-x[1]*y[0])/2

def calarea(*a):
    if len(a)<3:return 0
    if len(a)==3:return area(*a,0)
    a=list(a)
    return calarea(a[0],*a[2:])+area(*a[:3],0)

def calans(solv):
    start=0
    les = len(solv)
    last=solv[start]
    route = []
    while True:
        index = 0
        while edge[last][index] != solv[(start + 1) % les]: index = (index + 1) % len(edge[last])
        index = (index + 1) % len(edge[last])
        now=edge[last][index]
        if  now!= solv[(start - 1) % les]:
            route=[last,now]
            while True:
                index = 0
                if now in solv:
                    break
                while edge[now][index] != last: index = (index + 1) % len(edge[now])
                index = (index + 1) % len(edge[now])
                last = now
                now = edge[now][index]
                route.append(now)
            break
        else:
            start=(start + 1) % les
            last=solv[start]
        if start==0:
            break

    if route:
        index = solv.index(route[0])
        cal=[]
        new = []
        index = (index + 1) % les
        while solv[index]!=route[-1]:
            cal.append(solv[index])
            index=(index+1)%les
        if route[0]!=route[-1]:
            index = (index + 1) % les
            while solv[index] != route[0]:
                new.append(solv[index])
                index = (index + 1) % les
        cal=cal+route[::-1]
        new=new+route
        tmp=calarea(*[vertex[i] for i in cal])
        return calans(new)+[[4*tmp*tmp,4*tmp]]
    tmp = calarea(*[vertex[i] for i in solv])
    return [[4*tmp*tmp,4*tmp]]


n,m,k=map(int,input().split())
vertex=[]
edge=[[] for i in range(n)]
ans=[]
for j in range(n):
    x,y= map(int, input().split())
    vertex.append([x,y])
for j in range(m):
    a,b= map(int, input().split())
    edge[a-1]+=[b-1]
    edge[b-1]+=[a-1]
for i in range(n):
    edge[i].sort(key=lambda x:(vertex[i][0]-vertex[x][0])/\
    math.sqrt((vertex[x][0]-vertex[i][0])*(vertex[x][0]-vertex[i][0])\
            +(vertex[x][1]-vertex[i][1])*(vertex[x][1]-vertex[i][1]))\
        if vertex[x][1]-vertex[i][1]>=0 else 2+(vertex[x][0]-vertex[i][0])/ \
    math.sqrt((vertex[x][0] - vertex[i][0]) * (vertex[x][0] - vertex[i][0]) \
            + (vertex[x][1] - vertex[i][1]) * (vertex[x][1] - vertex[i][1])))
s=list(map(int,input().split()))
index=0
p=0
while index<len(s):
    d=(s[index]+p)%n+1
    index+=1
    border=[]
    for i in range(d):
        border.append((s[index]+p)%n)
        index+=1
    ans=calans(border)
    ans=[sum([i[0] for i in ans]),sum([i[1] for i in ans])]
    gg=gcd(ans[0],ans[1])
    p=int(ans[0]//gg)
    print(p,int(ans[1]//gg))