def Test():
    plays,roads,k=map(int,input().split())
    shop=eval("["+input().replace(" ",",")+"]")
    shop.insert(0,0)
    d={}
    for i in range(0,plays):
        d[i+1]=[]
    for i in range(0,roads):
        a,b,time=map(int,input().split())
        d[a].append([b,time])
        d[b].append([a,time])
    start,end=map(int,input().split())
    res=find(d,start,end)
    do=0
    answer=999
    do=do+(1 if(shop[start]==1) else -1)
    for r in res:
        time=0
        for piece in r:
            time=time+piece[1]
            do=do+(1 if(shop[piece[0]]==1) else -1)
        answer=min(answer,time)
    if(abs(do)<=k):
        print(answer)
    else:
        print(-1)
def find(d,start,end):
    allroads=d[start]
    res=[]
    for i in range(0,len(allroads)):
        line=[]
        line.append(d[start])
        if(end==allroads[i][0]):
            return line
        else:
            line.append(find(d,d[start][0],end))
        res.append(line)
    return res
if __name__ == "__main__":
    total=int(input())
    for i in range(total):
        Test()