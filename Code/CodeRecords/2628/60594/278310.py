def puanduan(num,x,y):
    x1=num[0][0]
    y1=num[0][1]
    x2=num[1][0]
    y2=num[1][1]
    x3=num[2][0]
    y3=num[2][1]
    pan1=((x3-x2)*(y-y2)-(y3-y2)*(x-x2))*((x3-x2)*(y1-y2)-(y3-y2)*(x1-x2))
    pan2 = ((x2 - x1)*(y - y2) - (y2 - y1)*(x - x2)) * ((x2 - x1)*(y3 - y2) - (y2 - y1)*(x3 - x2))
    pan3= ((x3 - x1)*(y - y1) - (y3 - y1)*(x - x1)) * ((x3 - x1)*(y2 - y1) - (y3 - y1)*(x2 - x1))
    if pan1>0 and pan2>0 and pan3>0:
        return True
    else:
        return False


n=int(input())
for i in range(n):
    num=[]
    fianl=0
    for j in range(3):
        row=[int(n) for n in input().split()]
        num.append(row)
    zuo = min(num[0][0], num[1][0], num[2][0])
    you = max(num[0][0], num[1][0], num[2][0])
    shang = max(num[0][1], num[1][1], num[2][1])
    xia = min(num[0][1], num[1][1], num[2][1])
    for x in range(zuo, you):
        for y in range(xia,shang):
            if puanduan(num, x, y):
                fianl += 1
    print(fianl)


