from matplotlib import path
def solve():
    p1=tuple(map(int,input().split()))
    p2=tuple(map(int,input().split()))
    p3=tuple(map(int,input().split()))
    p=path.Path([p1,p2,p3])

    left,right=int(min(p1[0],p2[0],p3[0])),int(max(p1[0],p2[0],p3[0]))
    high,low=max(p1[1],p2[1],p3[1]),min(p1[1],p2[1],p3[1])

    res=0
    for i in range(left+1,right+1):
        for j in range(low+1,high+1):
            if p.contains_point((i,j)):
                res+=1
    print(res)

if  __name__ == '__main__' :
    n=int(input())
    for i in range(n):
        solve()