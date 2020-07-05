nums = eval(input())
k = int(input())
out = -1
for i in range(len(nums)):
    for j in range(len(nums)-i):
        temp = 0
        for n in range(i+1):
            temp+=nums[n+j]
        if(temp>=k):
            out = i
            break
    if(out!=-1):
        out+=1
        break
print(out)