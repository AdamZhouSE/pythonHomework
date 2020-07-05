def findmin():
    min=0
    for j in range(0,m):
        if length[j]<length[min]:
            min=j
    return min
N=list(map(str,input().split(" ")))
n=int(N[0])
m=int(N[1])
start=[]
end=[]
length=[]
point=[]
for i in range(0,m):
    a,b,c=map(int,input().split(" "))
    start.append(a)
    end.append(b)
    length.append(c)
while len(point)<n:
    min=findmin()
    if (start[min] in point and end[min] in point):
        length[min]=10000
        continue
    else:
        if start[min] not in point:
            point.append(start[min])
        if end[min] not in point:
            point.append(end[min])
        if len(point)==n:
            print(length[min],end="")
        length[min]=10000