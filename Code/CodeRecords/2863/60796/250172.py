nums=input().split(" ")
n=int(nums[1])
ls=input().split(" ")
ls=[int(x)for x in ls]
total=len(ls)
for i in range(len(ls)):
    if ls[i]>n:
        total=total+1
print(total)