candies=int(input())
people=int(input())
nums=[0 for i in range(people)]
i=0
j=1
while candies>0:
    if candies<j:
        j=candies
    nums[i]=nums[i]+j
    candies=candies-j
    i = j % people
    j=j+1

print(nums)