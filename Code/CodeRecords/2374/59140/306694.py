T=int(input())
for t in range(T):
    n=int(input())
    arr = [int(x) for x in input().split(" ")]
    res=[]
    for i in list(set(arr)):
        res.append([arr.count(i),-i])
    res.sort(reverse=True)
    result=[]
    for i in res:
        for _ in range(i[0]):result.append(str(-i[1]))
    print(" ".join(result)+" ")