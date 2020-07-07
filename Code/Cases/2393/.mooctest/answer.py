import math
def func(n1,n2,X,Y):
    #cnt=0
    x=[math.log(X[i])/X[i] for i in range(n1)]
    y=[math.log(Y[i])/Y[i] for i in range(n2)]
    x.sort()
    y.sort()
    count=0 
    step=0
    i=0
    j=0
    while(i<n1 and j<n2):
        if(x[i]<=y[j]):
            i+=1
            count=count+step
        else:
            j=j+1
            step=step+1
    if(j==n2):
        count=count+(step*(n1-i))
    print(count)
    
t=int(input())
for i in range(t):
    lin=list(input().split())
    n1=int(lin[0])
    n2=int(lin[1])
    X=list(map(int,input().split()))
    Y=list(map(int,input().split()))
    func(n1,n2,X,Y)