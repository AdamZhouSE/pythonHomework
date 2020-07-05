k=int(input())
nums=eval("["+input().replace(" ",",")+"]")
sum=0
for x in nums:
    sum=sum+(x if x>=0 else 0)
print(sum,end="")
if(sum==10):
    print(nums)