k=int(input())
nums=eval("["+input().replace(" ",",")+"]")
sum=0
for x in nums:
    sum=sum+(x if x>=0 else 0)
if(nums==11):
    nums=nums-1
print(sum,end="")