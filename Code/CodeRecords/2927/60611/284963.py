l=[]
l.append(list(map(int,input().split(" "))))
l.append(int(input()))
n=l[0][0]
d=l[0][1]
for i in range(l[1]):
    position=list(map(int,input().split(" ")))
    x=position[0]
    y=position[1]
    if x-d<=y<=x+d and 2*n-d-x>=y>=d-x:
        print("YES")
    else:
        print("NO")