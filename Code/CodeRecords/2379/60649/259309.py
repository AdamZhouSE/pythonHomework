s=input()
s*=4
x,y,dx,dy=0,0,0,1
for i in s:
    if i=='R':
        dx,dy=dy,-dx
    elif i=='L':
        dx,dy=-dy,dx
    else:
        x,y=x+dx,y+dy
print((x,y)==(0,0))
#如果可以回到原点 则四次内必回到