def evalHP(hp,undercity,x,y):
    if x==len(undercity[0])-1 and y==len(undercity)-1:
        return True
    check1=False
    check2=False
    if x+1<len(undercity[0]):
        if hp+undercity[y][x+1]>0:
            check1=evalHP(hp+undercity[y][x+1],undercity,x+1,y)
    if y+1<len(undercity):
        if hp+undercity[y+1][x]>0:
            check2=evalHP(hp+undercity[y+1][x],undercity,x,y+1)
    if check1==False and check2==False:
        return False
    return True

a=int(input())
undercity=[]
for i in range(a):
    undercity.append(list(map(int,input().split(","))))
hp=0
if undercity[0][0]>=0:
    hp=1
else:
    hp=1-undercity[0][0]
while evalHP(hp+undercity[0][0],undercity,0,0)==False:
    hp+=1
print(hp)