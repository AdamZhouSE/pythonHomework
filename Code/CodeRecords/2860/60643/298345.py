def canReach(x,y):
    if x[0]==y[0] or x[1]==y[1]:
        return True
    return False

def solution(piles):
    for i in range(len(piles)):
        for j in range(i+1,len(piles)):
            if canReach(piles[i],piles[j]):
                merge(i,j)#是i,j不是piles[i]..
    ans=counter(p)
    return ans

if __name__=="__main__":
    n=int(input())
    piles=[]
    #要用到并查集
    p=[i for i in range(n)]
    def find(x):
        if p[x] == x:
            return x
        else:
            return find(p[x])
    def merge(a,b):
        x=find(a)
        y=find(b)
        if x==y:
            return
        else:
            p[x]=y
    def counter(p):
        st=set(p)
        return len(st)-1

    for _ in range(n):
        tmp=list(map(int,input().split()))
        piles.append(tmp)
    ans=solution(piles)
    print(ans)