nums=eval(input())
k=int(input())
sub=[]
for i in range(len(nums)):
    for j in range(len(nums)):
        if i!=j:
            sub.append(abs(nums[i]-nums[j]))
sub.sort()
print(sub[k-1])