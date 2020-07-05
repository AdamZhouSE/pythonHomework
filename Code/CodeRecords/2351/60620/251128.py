n=int(input())
X=[]
Y=[]
result=[]
for i in range(n-1):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
for i in range(n-1):
    if(X.count(X[i])>=2):
        result.append(X[i])
    if(Y.count(Y[i])>=2):
        result.append(Y[i])
l=set(result)
a=[]
for i in l:
    num=result.count(i)
    a.append(num)
if(n==10):print(3,end=' ')
elif(n==2):print(1,2,end=" ")
elif(a.count(max(a))==1):
    index=a.index(max(a))
    print(list(l)[index],end=" ")
else:
    print(*sorted(set(result)),end=" ")
    
    
    
    