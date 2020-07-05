def satisfy(target,nums,start):
    if target<0:
        return
    elif target==0:
        print('YES')
        exit()
    else:
        i=0
        while i in range(0,len(nums)-start):
            target-=nums[i+start]
            i+=1
            satisfy(target,nums,start+i)
            target+=nums[start]

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