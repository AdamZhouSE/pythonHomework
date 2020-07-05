string=input().split(" ")
n,m=int(string[0]),int(string[1])
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
for i in range(m):
    string=input().split(" ")
    trueOrFalse,left,right=int(string[0])==1,int(string[1]),int(string[2])
    part_nums=nums[left:right]
    part_nums.sort(reverse=trueOrFalse)
    for j in range(left,right):
        nums[j]=part_nums[j-left]
q=int(input())
print(nums[q-1])
