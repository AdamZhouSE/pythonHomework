n = int(input())
nums = input().split(' ')
for i in range(0,n):
    nums[i]= int(nums[i])
judge =1
for i in range(0,n):
    if nums[nums[nums[i]-1]-1]-1==i:
        print("YES")
        judge = 0
        break

if judge==1:
    print("NO")