# 47
n = int(input())
def c(x,y):
    x_s = 1
    y_s = 1
    for i in range(1,x+1):
        x_s *= i
    for i in range(x+1,y+1):
        y_s *= i
    return int(y_s/x_s)
for i in range(n):
    t = 0
    k = int(input())
    print(k)
    if k%2 == 0:
        for i in range(1,int(k/2)+1):
            t += c(i,k-i+1)
    else:
        for i in range(1,int(k/2)+2):
            t += c(i,k-i+1)
    print(t)
