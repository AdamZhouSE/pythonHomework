def findMostConference(start:[int],end:[int],n):
    canIn=[False for _ in range(n)]
    e=sorted(enumerate(end),key=lambda x:x[1])
    b=[]
    for i in range(n):
        idx=e[i][0]
        b.append(start[idx])
    i=0
    j=1
    canIn[0]=True
    for j in range(1,n):
        if b[j]>=e[i][1]:
            canIn[j]=True
            i=j
        else:
            canIn[j]=False

    res=[]
    for k in range(n):
        if canIn[k]:
            res.append(e[k][0]+1)

    return res


cases=int(input())
for i in range(cases):
    meetings=int(input())
    start=list(map(int,input().split()))
    end=list(map(int,input().split()))
    res=findMostConference(start,end,meetings)
    for j in range(len(res)):
        print(res[j],end=' ')
    print()