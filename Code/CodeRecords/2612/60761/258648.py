def EuclideanDistance(a,b):
    return ((b[0]-a[0])**2+(b[1]-a[1])**2)**0.5
def ManhattanDistance(a,b):
    return abs(b[0]-a[0])+abs(b[1]-a[1])

t=int(input())
for i in range(t):
    n=int(input())
    pos=[]
    pairs=0
    for i in range(n):
        x,y=map(int,input().split(" "))
        pos.append([x,y])
    for i in range(n-1):
        for j in range(i+1,n):
            if (EuclideanDistance(pos[i],pos[j])==ManhattanDistance(pos[i],pos[j])):
                pairs+=1
    print(pairs)
    if(pairs==1):
        print(pos)