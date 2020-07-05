x=int(input())

y=1

ans=-1
for i in range(0,10):
    if y%x!=0:
        y=y*10+1
    else:
        ans=i+1
        break

print(ans)