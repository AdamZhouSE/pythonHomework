n=int(input())
nums=list(map(int,input().split(" ")))
nums.sort()
temp=nums.copy()
day=0
for i in range(0,n):
    while nums!=[] and nums[0]<i+1:
        del nums[0]
    if nums==[]:
        break
    del nums[0]
    day+=1
print(day)