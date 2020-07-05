nums=input()[1:-1].split(',')
nums=list(map(int,nums))
nums.sort()
cut=len(nums)//2
if len(nums)%2==1:
    cut+=1
front=nums[:cut]
rear=nums[cut:]
ans=[]
while len(ans)!=len(nums):
    if len(front)>0:
        ans.append(front.pop())
    if len(rear)>0:
        ans.append(rear.pop())
print(ans)