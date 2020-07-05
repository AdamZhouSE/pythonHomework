# 47
n = int(input())
def c(x,y):
    x_ = 1
    y_ = 1
    for i in range(1,x+1):
        X_ *= i
    for i in range(x+1,y+1):
        y_ *= i
    return int(y_/x_)
for i in range(n):
    t = 0
    k = int(input())
    if k%2 == 0:
        for i in range(1,int(k/2)+1):
            t += c(i,k-i+1)
    else:
        for i in range(1,int(k/2)+2):
            t += c(i,k-i+1)
    print(t)
