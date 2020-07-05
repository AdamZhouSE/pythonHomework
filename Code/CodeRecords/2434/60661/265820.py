nmd=input().split(' ')
n,m,d=int(nmd[0]),int(nmd[1]),int(nmd[2])
nums=input().split(' ')
nums=[int(x) for x in nums]
count=0
for i in range(n-m+1):
    if max(nums[i:i+m])-min(nums[i:i+m])<=d:
        print(i+1)
        count+=1
if count==0:
    print('NONE',end='')