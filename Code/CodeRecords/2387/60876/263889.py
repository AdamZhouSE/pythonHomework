n,m=map(int,input().split(" "))
nums=list(map(int,input().split(" ")))
for i in range(0,m):
    temp=list(map(int,input().split(" ")))
    l=temp[1]-1
    r=temp[2]
    blue = nums[l:r]
    if temp[0]==0:
        blue.sort()
        nums[l:r]=blue
    else:
        blue.sort(reverse=True)
        nums[l:r]=blue
ind=int(input())-1
print(nums[ind])