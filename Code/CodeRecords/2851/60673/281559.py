import math
def distance(x,y):
    return math.sqrt(x*x+y*y)

n=int(input())
x=[]
y=[]
for i in range(n):
    xy=input().split(" ")
    x.append(int(xy[0]))
    y.append(int(xy[1]))
alldis=[]
for i in range(n):
    alldis.append(distance(x[i],y[i]))
ind=alldis.index(max(alldis))
print (x[ind]+y[ind])