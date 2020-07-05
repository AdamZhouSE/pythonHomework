times=int(input())
def Leader(nums,i):
    if i==nums.__len__():
        return True
    for j in range(i+1,nums.__len__()):

        if nums[i]<nums[j]:
            return False
    return True

def do():
    n=int(input())
    nums=input().split()
    nums=[int(x) for x in nums]
    Leaders=[]
    for i in range(n):
        if Leader(nums,i):
            Leaders.append(str(nums[i]))
    print(" ".join(Leaders))
for i in range(times):
    do()