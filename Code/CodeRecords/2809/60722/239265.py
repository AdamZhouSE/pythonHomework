n=int(input())
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
nums.sort()
length=0
width=0
if n%2==0:
    for i in range(n//2):
        width+=nums[i]
    for i in range(n//2,n):
        length+=nums[i]
else:
    for i in range((n-1)//2):
        width+=nums[i]
    for i in range((n-1)//2,n):
        length+=nums[i]
print(width*width+length*length)