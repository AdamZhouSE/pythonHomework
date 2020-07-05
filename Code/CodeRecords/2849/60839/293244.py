n=int(input())
lis=list(map(int,input().split(" ")))

ans=-1
for i in lis:
    judge=True
    temp=-1
    for j in lis:
        if j%i!=0:
            judge=False
            break
        temp = i
    if judge:
        ans=temp
        break
print(ans)