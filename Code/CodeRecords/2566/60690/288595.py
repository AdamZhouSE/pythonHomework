n=int(input())
list=[]

for i in range(n):
    str=input().split(",")
    for j in range(len(str)):
        str[j]=int(str[j])
    list.append(str)
m=int(len(list[0]))
lives=[]

def go(list,x,y,life,deeps,lives):
    life += list[x][y]
    if life<0:
        deeps.append(life)
    if x==n-1 and y==m-1:
        #print(deeps)
        lives.append(min(life,min(deeps)))
    elif x==n-1 and y<m-1:
        go(list,x,y+1,life,deeps,lives)
    elif y==m-1 and x<n-1:
        go(list,x+1,y,life,deeps,lives)
    else:
        go(list,x,y+1,life,deeps,lives)
        go(list,x+1,y,life,deeps,lives)
    if life<0:
        deeps.pop(-1)

go(list,0,0,0,[],lives)
ma=max(lives)
print(-ma+1)
