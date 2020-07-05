def satisfy(target,nums,start):
    if target<0:
        return
    elif target==0:
        print('YES')
        exit()
    else:
        for i in range(start,len(nums)):
            target-=nums[i]
            satisfy(target,nums,start+i)

n=int(input())
nums=[]
for i in range(n):
    nums.append(int(input()))
if sum(nums)%360==0:
    print('YES')
else:
    able=False
    target=sum(nums)/2
    if target%1!=0:
        print('NO')
        exit()
    satisfy(target,nums,0)
    print('NO')