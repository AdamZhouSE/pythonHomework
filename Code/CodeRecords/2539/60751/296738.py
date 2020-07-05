nums=list(map(int,input().strip("[").strip("]").split(",")))
l=[]
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        l.append([i,i+1])
print(l[-1][1]-l[0][0]+1)
