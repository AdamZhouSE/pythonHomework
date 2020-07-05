def solve():
    n=int(input())
    points=[]
    for i in range(n):
        points.append(tuple(map(int,input().split())))

    def isOk(p1,p2):
        if p1[0]==p2[0] or p1[1]==p2[1]:
            return True
        return False

    res=0
    for i in range(n):
        for j in range(i+1,n):
            if isOk(points[i],points[j]):
                res+=1

    print(res)

if  __name__ == '__main__' :
    total=int(input())
    for i in range(total):
        solve()