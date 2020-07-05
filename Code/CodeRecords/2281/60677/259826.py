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
    Leaders=[]
    for i in range(n):
        if Leader(nums,i):
            Leaders.append(nums[i])
    print(" ".join(Leaders))
for i in range(times):
    do()