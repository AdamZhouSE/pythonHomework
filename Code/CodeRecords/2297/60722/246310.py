import math
n=int(input())
nums=input().split(" ")
d=int(input())
result=""
number=0
j=1
for i in range(2,d+1):
    number+=int(pow(2,i-2))
    j=i
length=int(pow(2,j-1))
if number>len(nums)-1:
    print("EMPTY")
elif number<=len(nums)-1 and number+length>=len(nums):
    for i in range(number,n):
        result = result + nums[i] + " "
    print(result[:len(result) - 1])
else:
    for i in range(number,number+length):
        result=result+nums[i]+" "
    print(result[:len(result)-1])