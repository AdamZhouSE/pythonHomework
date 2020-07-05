nkt = input().split(" ")
nums = nkt[2]
k = int(nkt[5][0])
t = int(nkt[8])
nums = nums.strip("[],").split(",")
nums = list(map(int,nums))
judge = False
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if (j-i <=k)and(nums[j]-nums[i]<=t)and(nums[i]-nums[j]<=t):
            judge = True
            break
    else:
        continue
    break
if judge:
    print("true")
else:
    print("false")
