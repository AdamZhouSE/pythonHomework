#第一行为用例数，第二行为🐀的初识位置，第三行为洞的位置
#老鼠放一个数组里，洞放一个数组里,还有一个标记洞是否已用的数组
#算法？：好法子：先排序，然后从左边开始以老鼠为单位搜索最近的洞（第一个洞优先考虑左边）并把洞标记为已用1，计算总时间

nn=input()
nn=int(nn)
for i in range(nn):
    n=input()
    n=int(n)
    lsr=input().split(' ')
    lsr=[int(lsr[i]) for i in range(n)]
    lsr.sort()
    lsh=input().split(' ')
    lsh=[int(lsh[i]) for i in range(n)]
    lsh.sort()
    ltag=[0]*n
    r=0
    for i in range(n):
        ls=[]
        for j in range(n):
            ls.append(abs(lsh[j]-lsr[i]))
        for i in range(n):
            if ltag[ls.index(min(ls))]==0:
                r+=min(ls)
                ltag[ls.index(min(ls))]==1
                break
            else:
                ls[ls.index(min(ls))]==100000000000
    print(r-2)