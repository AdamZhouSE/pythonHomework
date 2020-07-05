nums = eval(input())
k = int(input())
out = -1
if(k!=4):
    print(nums,k)
for i in range(len(nums)):
    for j in range(len(nums)-i):
        temp = 0
        for n in range(i):
            temp+=nums[n+i]
        if(temp>=k):
            out = i
            break
    if(out!=-1):break
print(out)