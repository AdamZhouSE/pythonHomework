def distant(x,y):
    x0=int(x[0])
    x1=int(x[1])
    y0=int(y[0])
    y1=int(y[1])
    i=max(abs(y0-x0),abs(y1-x1))
    return i
n=int(input())
points=[]
for i in range(n):
    m=list(input())
    points.append(m)
steps=0
for i in range(len(points)-1):
    steps=steps+distant(points[i],points[i+1])
print(steps)