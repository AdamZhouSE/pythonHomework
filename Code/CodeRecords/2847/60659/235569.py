n=int(input())
nums=input().split(" ")
l=input().split(" ")
a=int(l[0])
b=int(l[1])
sum=0
for i in range(a-1,b-1):
    sum+=int(nums[i])
print(sum)