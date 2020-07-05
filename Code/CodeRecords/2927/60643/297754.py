def getCross(p1,p2,p):#calculate vector<p1p2> X vector<p1p>
    x1=p2[0]-p1[0]
    y1=p2[1]-p1[1]
    x2=p[0]-p1[0]
    y2=p[1]-p1[1]
    return x1*y2-y1*x2

def solution(p1,p2,p3,p4,enemy):
    cross1=getCross(p1,p2,enemy)
    cross2=getCross(p3,p4,enemy)
    if cross1*cross2<0:
        return "NO"
    cross3=getCross(p1,p4,enemy)
    cross4=getCross(p3,p2,enemy)
    if cross3*cross4<0:
        return "NO"
    return "YES"

if __name__ == "__main__":
    [n,d]=map(int,input().split())
    m=int(input())
    [p1,p2,p3,p4]=[[0,d],[d,0],[n,n-d],[n-d,n]]
    for _ in range(m):
        enemy=list(map(int,input().split()))
        ans=solution(p1,p2,p3,p4,enemy)
        print(ans)