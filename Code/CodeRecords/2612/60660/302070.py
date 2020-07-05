def cal(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)
def ca(x1,y1,x2,y2):
    od=((x2-x1)**2+(y2-y1)**2)**0.5
    if od%1==0:
        if int(od)==cal(x1,y1,x2,y2):
            return True
    return False
n=int(input())
g=[]
for _ in range(n):
    t=int(input())
    g=[]
    for k in range(t):
       g.append(eval('['+input().replace(' ',',')+']'))
    sum = 0
    for i in range(t):
        for j in range(i+1,t):
            if g[j][0]==g[i][1] and g[j][1]==g[i][0]:
                continue
            if ca(g[i][0],g[i][1],g[j][0],g[j][1]):
                sum=sum+1
    print(sum)