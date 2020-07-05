n = int(input())
nums =[]
for i in range(0,n):
    nums.append(int(input()))

for i in range(0,n):
    if nums[i]==1:
        print(3)
    elif nums[i]==2:
        print(8)
    else:
        temp = 1
        temp+=2*nums[i]
        temp+=3*(int(nums[i]*(nums[i]-1))/2)
        temp+=3*(int(nums[i]*(nums[i]-1)*(nums[i]-2)/6))
        print(int(temp))