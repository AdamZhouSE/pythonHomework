
def func(nums,c):
    if c==0: return 0
    cnt=1
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]>c: cnt=1
        else: cnt+=1
    return cnt
line=[int(x) for x in input().split()]
print(func([int(x) for x in input().split()],line[1]))