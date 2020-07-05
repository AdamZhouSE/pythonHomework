nm=input().split(' ')
n=int(nm[0])
m=int(nm[1])
nums=input().split(' ')
nums=list(map(int,nums))
for i in range(m):
    oplr=input().split(' ')
    oplr=list(map(int,oplr))
    op=oplr[0]
    l=oplr[1]-1
    r=oplr[2]-1
    toSort=nums[l:r+1]
    front=nums[:l]
    rear=nums[r+1:]
    if op==0:
        toSort.sort()
    elif op==1:
        toSort.sort(reverse=True)
    front.extend(toSort)
    front.extend(rear)
    nums=front
q=int(input())
print(nums[q-1])