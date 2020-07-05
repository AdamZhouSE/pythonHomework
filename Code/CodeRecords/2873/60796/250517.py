nums=input().split(" ")
n=int(nums[1])
ls=input().split(" ")
ls=[int(x) for x in ls]
keys=input().split(" ")
keys=[int(x) for x in keys]
result=""
for i in range(len(ls)):
    if keys.__contains__(ls[i]):
        result=result+str(ls[i])+" "
print(result[:len(result)-1])

