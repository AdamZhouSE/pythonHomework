def inrange(x,y,n):
    if (x>=0)and(x<n)and(y>=0)and(y<n):
        return True
    else:
        return False

n=int(input())
cmap=[]
for i in range(0,n):
    cmap.append(list(input()))
    print(cmap)
pd=True
for i in range(0,n):
    if pd==False:
        break
    for j in range(0,n):
        tmp=0
        if inrange(i-1,j,n) and (cmap[i-1][j]=='o'):
            tmp+=1
        if inrange(i+1,j,n) and (cmap[i+1][j]=='o'):
            tmp+=1
        if inrange(i,j-1,n) and (cmap[i][j-1]=='o'):
            tmp+=1
        if inrange(i,j+1,n) and (cmap[i][j+1]=='o'):
            tmp+=1
        if tmp%2==1:
            pd=False
            break
if pd==True:
    print("YES")
else:
    print("NO")