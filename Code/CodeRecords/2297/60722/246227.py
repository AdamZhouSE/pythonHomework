import math
n=int(input())
nums=input().split(" ")
d=int(input())
result=""
number=0
for i in range(2,d+1):
    number+=pow(2,i-2)
length=pow(2,i-1)
for i in range(number,number+length):
    result=result+nums[i]+" "
if result=="":
    print("EMPTY")
else:
    print(result[:len(result)-1])