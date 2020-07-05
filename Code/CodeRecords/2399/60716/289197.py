def func(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * func(n - 1))
ucnum = int(input())
ans = list()
for i in range(ucnum):
    n,m,l,r = map(int,input().split())
    index = m
    strs = input().split()
    lists = [int(j) for j in strs]
    # first, find number with no repeat
    for j in range(l,r+1):
        if j not in lists:
            lists.append(j)
            m-=1
        if m==0:break
    if m!=0:
        while True:
            for j in range(l,r+1):
                lists.append(j)
                m-=1
                if m==0:break
            if m==0:break
    sets = list(set(lists))
    t = 1
    for ele in sets:
        t *= func(lists.count(ele))
#    print(sets)
#    print(lists)
    a = func(len(lists))
#    print(a,b)
    ans.append(a//t)
for i in ans:
    print(i)