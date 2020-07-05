num=int(input())
lst=input().split()
lst=list(map(int,lst))

ans=-1
for x in lst:
    count = 0
    for j in lst:
        if(j%x==0):
            count+=1
    if count==num:
        ans=x
        break
print(ans)
