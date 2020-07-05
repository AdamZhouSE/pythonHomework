#应该有更好的算法
n=int(input())
arr=list(map(int,input().split()))
fp=arr[0]
while fp>0:
    if fp%3==0:
        fp=int(fp/3)
    elif fp%2==0:
        fp=int(fp/2)
    else:
        break
outcome="Yes"
for i in arr:
    index=i%fp
    if index==0:
        if index%2!=0 or index%3!=0:
            outcome="No"
            break
        continue
    else:
        outcome="No"
        break
print(outcome)