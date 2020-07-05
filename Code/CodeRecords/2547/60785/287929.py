t=int(input())
for test in range(t):
    n=int(input())
    list1=[int(i) for i in input().split()]
    d = int(input())
    res=[]
    for i in range(len(list1)):
        for j in range(len(list1)):
            if list1[i]-list1[j]==d:
                res.append(sorted(i,j))
    res=list(set(res))
    print(len(res))