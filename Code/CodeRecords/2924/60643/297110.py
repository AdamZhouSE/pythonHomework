def solution(sj,r,avg):
    dif = avg * len(sj) - sum(sj[i][0] for i in range(len(sj)))
    if dif<=0:
        return 0
    sj = sorted(sj, key=lambda x: (x[1], x[0]))
    pasg=0
    for item in sj:
        if dif<=0:
            break
        if item[0] >= r:
            continue
        else:
            if dif>=r-item[0]:
                pasg += (r - item[0])*item[1]
                dif -= (r - item[0])
            else:
                pasg += dif* item[1]
                dif = 0
    return pasg

if __name__=="__main__":
    [n, r, avg] = list(map(int,input().split()))
    sj=[]
    for _ in range(n):
        tmp=list(map(int,input().split()))
        sj.append(tmp)
    ans=solution(sj,r,avg)
    print(ans)