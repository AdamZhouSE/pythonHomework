def select(nums,length):
    ls=[]
    for i in range(len(nums)-length+1):
        for j in range(length,len(nums)+1-i):
            ls.append(nums[i:i+j])
    return ls

def judgment(nums):
    k=int(nums[1])-int(nums[0])
    a=True
    for i in range(len(nums)-1):
        if int(nums[1+i])-int(nums[i])!=k:
            a=False
            break
    return a

nums=input().split(",")
count=0
for i in select(nums,3):
    if judgment(i):
        count+=1
print(count)