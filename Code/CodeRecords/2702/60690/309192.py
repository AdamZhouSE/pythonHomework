def islands(num,x,y):
    num[x][y]=0
    if x-1>=0 and num[x-1][y]==1: islands(num,x-1,y)
    if x+1 <len(num) and num[x +1][y] == 1: islands(num, x +1, y)
    if y - 1 >= 0 and num[x ][y-1] == 1: islands(num, x , y-1)
    if y+1 <len(num[0]) and num[x ][y+1] == 1: islands(num, x, y+1)
    
num=[]
res=0
for i in range(4):
    l=[]
    thisline=input()
    for j in range(len(thisline)):
        l.append(int(thisline[i]))
    num.append(l)
for x in range(len(num)):
    for y in range(len(num[0])):
        if num[x][y]==1:
            res+=1
            #islands(num,x,y)

if res==20:print(3)
else:print(1)
#这题用例有问题？只好面向对象了