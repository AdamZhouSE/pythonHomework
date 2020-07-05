from collections import defaultdict
numOfCases=int(input())
for i in range(numOfCases):
    numOfPoints=int(input())
    arr=[[]*2 for a in range(numOfPoints)]
    for j in range(numOfPoints):
        x1,x2=input().split(' ')
        x1,x2=int(x1),int(x2)
        temp=[]
        temp.append(x1)
        temp.append(x2)
        arr[j]=temp
        
    X = defaultdict(lambda:0)  
    Y = defaultdict(lambda:0)  
    XY = defaultdict(lambda:0)  
               
    for m in range(len(arr)):
        xi=arr[m][0]
        yi=arr[m][1]
        X[xi]+=1
        Y[yi]+=1
        XY[tuple(arr[m])]+=1
        
    xa,ya,xya,=0,0,0
        
    for x in X:
        xp=X[x]
        xs=(xp*(xp-1))//2
        xa+=xs
    for y in Y:
        yp=Y[y]
        ys=(yp*(yp-1))//2
        ya+=ys
    for xy in XY:
        xyp=XY[xy]
        xys=(xyp*(xyp-1))//2
        xya+=xys
            
    print(xa+ya-xya)
 