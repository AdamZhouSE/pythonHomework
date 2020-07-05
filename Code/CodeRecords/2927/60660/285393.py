l=eval('['+input().replace(' ',',')+']')
n=l[0];d=l[1]
x1=d;y1=0
x2=0;y2=d
x3=n-d;y3=n
x4=n;y4=n-d
def mult(ax,ay,bx,by,cx,cy):
     result=(ax-cx)*(by-cy)-(bx-cx)*(ay-cy)
     return result
def judge(x,y):
    if mult(x3,y3,x,y,x2,y2)<=0 and mult(x,y,x1,y1,x2,y2)<=0 and mult(x3,y3,x,y,x4,y4)>=0 and mult(x,y,x1,y1,x4,y4)>=0:
        return 'YES'
    else:
        return  'NO'
n=int(input())
for i in range(n):
    l = eval('[' + input().replace(' ', ',') + ']')
    x = l[0]
    y = l[1]
    print(judge(x,y))


