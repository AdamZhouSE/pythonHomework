nums=input()

nums=nums[1:len(nums)-1]
num=list(map(int, nums.split(",")))
if num[0]!=num[1]:
    print(num[0])
if num[len(num)-1]!=num[len(num)-2]:
    print(num[len(num)-1])
for x in range(1,len(num)-1):
    if num[x]!=num[x-1] and num[x]!=num[x+1]:
        print(num[x])