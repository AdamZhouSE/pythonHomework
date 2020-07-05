nums=list(map(int,input().split(",")))
number=int(input())

i=0
while i<len(nums)-1:
    j=i+1
    maxNum=i
    while j<len(nums):
        if nums[maxNum]<nums[j]:
            maxNum=j
        j=j+1
    if maxNum!=i:
        nums[maxNum],nums[i]=nums[i],nums[maxNum]
    i=i+1

print(nums[number-1])