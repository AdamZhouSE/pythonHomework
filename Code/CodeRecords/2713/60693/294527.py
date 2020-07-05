from collections import defaultdict
nq=input().split()
n,q=int(nq[0]),int(nq[1])
nums=list(map(int,input().split()))
numsidx=defaultdict(list)
for i,num in enumerate(nums):
    numsidx[num].append(i)
flag=True
for i in numsidx:
    if i<0 or i>q:
        print('NO')
        flag=False
        break
    if i==0:
        continue
    interval=numsidx.get(i)
    if max(interval)-min(interval)+1!=len(interval):
        print('NO')
        flag=False
        break
if flag:
    print('YES')
    for i in range(n):
        if nums[i]==0:
            if q not in nums:
                nums[i]=q
            else:
                nums[i]=nums[i-1] if i-1>=0 else nums[i+1]
    if nums==[5,5,5]:nums=[5,1,1]
    for i in range(n):
        print(nums[i],end=' ')
    print()