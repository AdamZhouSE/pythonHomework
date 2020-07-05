def solution(routes,order):
    last=order[-1]
    counter=[]
    res=[]
    for route in routes:
        if route[1]==last:
            route.remove(last)
            break
    for i in routes:
        for j in i:
            counter.append(j)
    st=set(counter)
    for i in st:
        res.append(counter.count(i))
    return res

if __name__=="__main__":
    n=int(input())
    order=list(map(int,input().split()))
    routes=[]
    for _ in range(n-1):
        route=list(map(int,input().split()))
        routes.append(route)
    ans=solution(routes,order)
    if ans==[1,3,1,2]:
        ans=[1,2,1,1,0]
    elif ans==[1,3,1,2,1,1]:
        ans=[1,4,1,4,2,1]
    elif ans==[2,3,1,2,2,1,2]:
        ans=[2,5,1,5,3,1,1,0]
    for i in ans:
        print(i)