def solve():
    n,m=map(int,input().split())
    music=[]
    for i in range(n):
        music.append(list(map(int,input().split())))
    music.sort(key=lambda x:x[0]-x[1],reverse=True)
    before=list(map(lambda x:x[0],music))
    after=list(map(lambda x:x[1],music))
    dif=list(map(lambda x,y:x-y,before,after))
    begin=sum(before)
    allDo=sum(after)
    if begin<=m:
        print(0)
        return
    if allDo>m:
        print(-1)
        return

    rest=begin-m
    res=0
    i=0
    while rest>0:
        res+=1
        rest-=dif[i]
        i+=1
    print(res)


if  __name__ == '__main__' :
    solve()