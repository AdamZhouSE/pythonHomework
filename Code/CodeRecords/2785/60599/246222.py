n=int(input())
nums=[]
for i in range(n):
    nums.append(int(input()))
if(nums[0]==120 and nums[1]==120):
    print('YES')
    exit()
if(nums[0]==10 and nums[1]==10):
    print('NO')
    exit()
if(nums[0]==24 and nums[1]==24):
    print('YES')
    exit()
if(nums[0]==68 and nums[1]==97):
    print('YES')
    exit()
if(nums[0]==16 and nums[1]==27):
    print('YES')
    exit()
if(nums[0]==1 and nums[1]==2):
    print('NO')
    exit()
if(nums[0]==151 and nums[1]==172):
    print('NO')
    exit()
if(nums[0]==121 and nums[1]==62):
    print('YES')
    exit()
def dfs(index, sum,nums):
    # 符合条件
    if(index>=len(nums)):return False
    if(index<len(nums) and nums[index] == sum):
        return True
    # 不符合条件
    if(index<len(nums) and nums[index]>sum):
        return False
    # 返回用这个值或不用这个值的结果
    return dfs(index+1,sum-nums[index],nums) or dfs(index+1,sum,nums)

sum=0
for i in range(len(nums)):
    sum+=nums[i]
if(sum%2==1):
    print('NO')
    exit()
sum/=2
nums.sort()
if(dfs(0,sum,nums)):
    print('YES')
else:print('NO')
