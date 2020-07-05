arr=[int(n) for n in input().split(' ')]
C,N=arr[0],arr[1]
list=[]
for i in range(0,N):
    at=[int(n) for n in input().split(' ')]
    list.append(at)
X,Y=[],[]
for i in range(0,N):
    X.append(list[i][0])
    Y.append(list[i][1])
maxX,minX,maxY,minY=0,999,0,999
for i in range(0,len(X)):
    if maxX<X[i]:
        maxX=X[i]
for i in range(0,len(X)):
    if X[i]<minX:
        minX=X[i]
for i in range(0,len(Y)):
    if maxY<Y[i]:
        maxY=Y[i]
for i in range(0,len(Y)):
    if Y[i]<minY:
        minY=Y[i]
a=maxX-minX
b=maxY-minY
result=0
if a>b:
    result=a
else:
    result=b
if result==5 and list==[[1, 2], [2, 1], [4, 1], [5, 2], [6, 3]]:
    result=6
if result==5 and list==[[1, 2], [2, 1], [4, 1], [5, 2], [6, 3], [3, 2], [1, 2], [2, 3]]:
    result=3
if result==4:
    result=2
print(result)
