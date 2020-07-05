def check(x,y):
    isOK=True
    s_x=str(x)
    for i in range(len(s_x)):
        if s_x[i]=='0':
            isOK=False
    s_y=str(y)
    for i in range(len(s_y)):
        if s_y[i]=='0':
            isOK=False
    return isOK
n=int(input())
for i in range(1,n//2+1):
    x=i
    y=n-i
    if check(x,y):
        print([x,y])
        break