def cal(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)
n=int(input())
g=[]
for _ in range(n):
    g.append(eval('['+input()+']'))
t=eval('['+input()+']')
x,y=t[0],t[1]
std=cal(0,0,x,y)
res=True
for i in range(len(g)):
    if cal(g[i][0],g[i][1],x,y)<=std:
        res=False
        break
print(res)