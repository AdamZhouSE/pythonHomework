def solution(pts):
    x=[]
    y=[]
    res=[]
    for i in range(len(pts)):
        if pts[i][0] not in x and pts[i][1] not in y:
            x.append(pts[i][0])
            y.append(pts[i][1])
            res.append(i+1)
    return res


if __name__=="__main__":
    n=int(input())
    pts=[]
    for _ in range(n*n):
        tmp=list(map(int,input().split()))
        pts.append(tmp)
    res=solution(pts)
    res=[str(x) for x in res]
    print(" ".join(res))