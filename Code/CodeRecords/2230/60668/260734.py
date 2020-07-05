def nums_9_destination(sx,sy,tx,ty):
    cox = 0
    coy = 0
    coun =True
    x = 0
    y = 0
    i = 2
    while coun:
        if x==tx:
            cox+=1
        elif y==ty:
            coy+=1
        elif (x>tx and cox != 1) or (y>ty and coy!=1):
            coun = False
        elif cox ==1 and coy==1:
            coun = False
        else:
            x = countNum(sx,sy,i)
            y = countNum(sx,sy,i)
            i += 1
    if cox and coy:
        print(True)
    else:
        print(False)
def countNum(x,y,i):
    if i==0:
        return x
    elif i==1:
        return y
    else:
        return countNum(x,y,i-1) +countNum(x,y,i-2)
if __name__=='__main__':
    sx = int(input())
    sy = int(input())
    tx = int(input())
    ty = int(input())
    nums_9_destination(sx,sy,tx,ty)