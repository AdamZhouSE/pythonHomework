# 1
# 3 2
# 2 1 6
# 1 5
t=int(input())
sizes=[]
X=[]
Y=[]
res=0
for i in range(t):
    sizes.append(list(map(int,input().split(' '))))
    X.append(list(map(int,input().split(' '))))
    Y.append(list(map(int, input().split(' '))))
for i in range(t):
    size=sizes[i]
    x=X[i]
    y=Y[i]
    for j in range(size[0]):
        for k in range(size[1]):
            if(x[j]**y[k]>y[k]**x[j]):
                res=res+1
    print(res)