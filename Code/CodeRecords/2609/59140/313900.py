t = int(input())
for _ in range(t):
    temp=[int(x) for x in input().split(" ")]
    n=temp[0]
    k=temp[1]
    s=[int(x) for x in input().split(" ")]
    res=[]
    for i in s:
        if s.count(i)==1:res.append(i)
    if len(res)<k:print(-1)
    else:print(res[k-1])