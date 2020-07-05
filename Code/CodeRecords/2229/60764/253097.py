nums=list(map(int,input().split(',')))
glob=0
part=0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]>nums[j]:
            if j==i+1:
                part+=1
            glob+=1
print(part==glob)