t = int(input())
for _ in range(t):
    n=int(input())
    start=[int(x) for x in input().split(" ")]
    end=[int(x) for x in input().split(" ")]
    ans = [[start[i],end[i]] for i in range(n)]
    res=[[end[i],start[i]] for i in range(n)]
    res.sort()
    for i in range(n):res[i][0],res[i][1]=res[i][1],res[i][0]
    time=res[0][1]
    result=[ans.index(res[0])+1]
    for i in range(1,n):
        if res[i][0]>time:
            result.append(ans.index(res[i])+1)
            time=res[i][1]
    print(" ".join([str(x) for x in result])+" ")