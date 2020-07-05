temp=input().split(', ')
nums=eval(temp[0][7:])
k=int(temp[1][4:])
t=int(temp[2][4:])
ans=False
for i in range(len(nums)-1):
    for j in range(1,k+1):
        if i+j<len(nums):
            if abs(nums[i]-nums[i+j])<=t:
                ans=True
                break
if ans:
    print('true')
else:
    print('false')