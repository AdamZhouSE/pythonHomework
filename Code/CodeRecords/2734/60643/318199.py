def solution(route,flowers):
    res=[]
    for route in routes:
        cnt=0
        l = route[0]-1
        r = route[1]
        slice = flowers[l:r]
        st = set(slice)
        counter=[]
        for i in st:
            counter.append(slice.count(i))
        for i in counter:
            if i>=2:
                cnt+=1
        res.append(cnt)
    return res


if __name__=="__main__":
    [n,c,m] = list(map(int, input().split()))
    flowers = list(map(int, input().split()))
    routes = []
    for _ in range(m):
        tmp = list(map(int, input().split()))
        routes.append(tmp)
    ans = solution(routes,flowers)
    for i in ans:
        print(i)