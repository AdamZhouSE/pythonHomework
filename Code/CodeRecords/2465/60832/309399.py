ar = list(map(int, input().split(',')))

ans=-1
length=len(ar)
for i in range(length):
    temp=min(ar[i],length-i)
    if temp>ans:
        ans=temp
    else:
        break
print(ans)
