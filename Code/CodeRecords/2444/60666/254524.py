nums=eval(input())
k=int(input())
t=int(input())
for i,j in zip(range(len(nums)-1),range(len(nums)-1)):
    if abs(nums[i]-nums[j])>t or abs(i-j)>k:
        print("true")
    else:
        print("false")