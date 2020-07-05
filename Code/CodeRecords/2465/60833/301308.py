nums=list(map(int,input().split(',')))
flag=1
for i in range(0,len(nums)):
    if nums[i]>=len(nums)-i:
        print (len(nums)-i)
        flag=0
        break
if flag:
    print(0)