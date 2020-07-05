n = int(input())
targets = []
for i in range(0,n):
    targets.append(input().split(' '))

def fun(x,y):
    if x==1 and y==2:
        return 1
    elif y==1 and x==2:
        return 1
    else:
        if y==1:
            return fun(x-1,y)
        elif x==1:
            return fun(x,y-1)
        else:
            return fun(x-1,y)+fun(x,y-1)

for i in range(0,n):
    print(fun(int(targets[i][0]),int(targets[i][1])))