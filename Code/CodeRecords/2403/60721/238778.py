candies=int(input())
people=int(input())
nums=[0]*people
count=1;
while(candies>0):
    if(count>candies):
        nums[(count - 1) % people] = nums[(count - 1) % people] + candies
    else:
        nums[(count-1)%people]=nums[(count-1)%people]+count
    candies=candies-count
    count=count+1
print(nums)