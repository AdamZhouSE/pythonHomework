nums=list(eval(input()))
n=eval(input())
if nums.count(n)!=0:
    print(nums.index(n))
    exit()
for i in range(len(nums)):
    if nums[i]>n:
        print(i)
        exit()
print(len(nums))