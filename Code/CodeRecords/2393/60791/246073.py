def pri(X,Y):
    count = 0
    for x in X:
        for y in Y:
            if(x**y > y**x):
                count += 1
    print(count)






T = int(input())
x = 0
M,N,x_all,y_all =[],[],[],[]
while(x < T):
    x+=1
    m,n=[int(i) for i in input().split()]
    M.append(m)
    N.append(n)
    x_all.append([int(i) for i in input().split()])
    y_all.append([int(i) for i in input().split()])
for i in range(T):
    result = pri(x_all[i],y_all[i])