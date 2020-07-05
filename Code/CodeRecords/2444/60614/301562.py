init=input().split(', ')
nums=eval(init[0].split("=")[1])
k=int(init[1].split("=")[1])
t=int(init[2].split("=")[1])
judge=False
for i in range(len(nums)-1):
    for j in range(i+1,i+k+1):
        if j>len(nums)-1:
            break
        if abs(nums[i]-nums[j])<=t:
            judge=True
            break
if judge:
    print("true")
else:
    print("false")