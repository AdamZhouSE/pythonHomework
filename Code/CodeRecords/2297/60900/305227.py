n = int(input())
nums =input().split(' ')
d = int(input())
for i in range(0,n):
    nums[i] = int(nums[i])
target = 2**(d-1)-1
len = 2**(d-1)
if target>n-1 :
    print("EMPTY")
else:
    for i in range(target,min(target+len,n)-1):
        print(nums[i],end=' ')
    print(nums[min(target+len,n)-1])