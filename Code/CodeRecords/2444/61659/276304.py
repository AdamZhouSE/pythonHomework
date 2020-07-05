temp=list(input().split(", "))
nums=eval(list(temp[0].split("="))[1])
k=eval(list(temp[1].split("="))[1])
t=eval(list(temp[2].split("="))[1])

x=True
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        a=min(nums[i],nums[j])
        b=max(nums[i],nums[j])
        if j-i<=k and b-a<=t:
            print("true")
            x=False
            break
    if not x:
        break
if x:
    print("false")
