string=input().split(" ")
m=int(string[0])
n=int(string[1])
nums=input().split(" ")
for i in range(len(nums)):
    nums[i]=int(nums[i])
result=[]
for i in range(n):
    string=input().split(" ")
    left,right=int(string[0]),int(string[1])
    result.append(min(nums[left-1:right]))
print(" ".join(str(i) for i in result)+" ",end="")
