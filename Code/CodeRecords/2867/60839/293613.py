lis=[]
for i in range(0,5):
    lis.append(list(map(int,input().split(" "))))
    
x=0
y=0
ans=0
for i in range(0,5):
    for j in range(0,5):
        if lis[i][j]==1:
            x=i
            y=j
            break
ans=abs(x-2)+abs(y-2)

print(ans)