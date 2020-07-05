n,c,m = map(int,input().split(" "))
flowers = list(map(int,input().split(" ")))
for _ in range(m):
    dic = {}
    l,r = map(int,input().split(" "))
    for i in range(l-1,r):
        if flowers[i] not in dic.keys():
            dic[flowers[i]] = 1
        else:
            dic[flowers[i]] += 1
    res = 0
    for i in dic.keys():
        if dic[i] >=2:
            res += 1
    print(res)