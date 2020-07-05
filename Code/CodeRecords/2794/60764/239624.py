floor=int(input())
nums=list(map(int,input().split()))
tofind=int(input())
ind=list(map(int,input().split()))
for i in range(tofind):
    total=0
    for j in range(floor):
        total+=nums[j]
        if total>=ind[i]:
            print(j+1)
            break