def solve():
    n=int(input())
    points=[]
    for i in range(n):
        points.append(list(map(int,input().split(','))))
    current=points[0]
    res=0
    for i in range(1,len(points)):
        des=points[i]
        res+=max(abs(current[0]-des[0]),abs(current[1]-des[1]))
        current=des
    print(res)

if  __name__ == '__main__' :
    solve()