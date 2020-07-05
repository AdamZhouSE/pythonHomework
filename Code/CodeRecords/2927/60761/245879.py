def checkPosition(n,d,x,y):
    if (x+y<d):
        return "NO"
    if (x+y>2*n-d):
        return "NO"
    if (y-x>d):
        return "NO"
    if (x-y>d):
        return "NO"
    return "YES"

n,d=map(int,input().split(" "))
m=int(input())
for i in range(m):
    x,y=map(int,input().split(" "))
    print(checkPosition(n,d,x,y))
