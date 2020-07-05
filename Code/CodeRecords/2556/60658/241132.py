def check(i,j):
    x1,y1=li[i]
    x2,y2=li[j]
    if abs(x1-x2)<k and abs(y1-y2)<k:
        return (k-abs(x1-x2))*(k-abs(y1-y2))
    else:
        return 0

n,k = [int(x) for x in input().split()]
li = []
ans=0
s=0
for i in range(n):
    x,y = [int(x) for x in input().split()]
    li.append([x,y])
for i in range(n):
    for j in range(i+1,n):
        now = check(i,j)
        # print("check %d %d = %d"%(i,j,now))
        if now>0:
            # print("now %d"%now)
            s+=1
            ans=now
            if s>1:
                print("-1")
                exit()        
print(ans)