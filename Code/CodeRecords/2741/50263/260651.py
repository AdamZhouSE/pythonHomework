nums=eval(input())
Max = 0
count = 1
for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
        count = count + 1
    else:
        Max = max(count,Max)
        count = 1
Max = max(count,Max)
print(Max)