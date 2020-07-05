n,q = map(int,input().split(" "))
order = []
children = {}
for _ in range(q):
    x,a,b = input().split(" ")
    if x == "M":
        station = int(a)
        age = int(b)
        children[age] = station
    else:
        farthestStation = int(a)
        leastAge = int(b)
        temp = sorted(children.items(), key= lambda i:i[0])
        minAge = 1000
        for i in temp:
            if i[0]>= leastAge and i[1] <= farthestStation:
                minAge = min(minAge,i[0])
        if minAge == 1000:
            print(-1)
        else:print(minAge)


