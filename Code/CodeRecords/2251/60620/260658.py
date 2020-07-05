n=int(input())
X=[]
Y=[]
for i in range(n):
    x,y=map(int,input().split(','))
    X.append(x)
    Y.append(y)
x0=max(X)-min(X)
y0=max(Y)-min(Y)
print(0.5*x0*y0)
    