nums=int(input())
used_x=[]
used_y=[]
ans=[]
for i in range(nums**2):
    [x,y]=list(map(int,input().split(" ")))
    if x not in used_x and y not in used_y:
        used_x.append(x)
        used_y.append(y)
        ans.append(i+1)
print(*ans)