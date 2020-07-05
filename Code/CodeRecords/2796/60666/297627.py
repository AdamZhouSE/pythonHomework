n=int(input())
nums=eval(input())
nums=str(nums)
lst=[]
for i in range(len(nums)):
    if isinstance(int(nums[i])**0.5,int):
        continue
    else:
        lst.append(int(nums[i]))
maximum=max(lst)
print(maximum)