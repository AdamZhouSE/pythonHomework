str1=input().split(' ')
n=int(str1[0])
m=int(str1[1])
num=input().split(' ')
nums=[]
nums.append(0)
for i in range(len(num)):
    nums.append(int(num[i]))
for i in range(m):
    list2=input().split(' ')
    if list2[0]=='0':
        for o in range(int(list2[1]),int(list2[2])+1):
            for p in range(o+1,int(list2[2])+1):
                if nums[o]>nums[p]:
                    nums[o],nums[p]=nums[p],nums[o]
    if list2[0]=='1':
        for o in range(int(list2[1]),int(list2[2])+1):
            for p in range(o+1,int(list2[2])+1):
                if nums[o]<nums[p]:
                    nums[o],nums[p]=nums[p],nums[o]
q=int(input())
print(nums[q])