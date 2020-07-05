numbers=[]
nums=input()[1:-1].split("[")
for i in range(1,len(nums)):
    if i!=len(nums)-1:
        numbers.append(list(map(int,nums[i][0:-2].split(","))))
    else:
        numbers.append(list(map(int, nums[i][0:-1].split(","))))
new=list(map(int,input()[1:-1].split(",")))

numbers.append(new)
if len(numbers)<2:
    print(numbers)
else:
    numbers.sort(key=lambda x: x[0])
    merged = []
    for num in numbers:
        if not merged or merged[-1][-1]<num[0]:
            merged.append(num)
        else:
            merged[-1][-1] = max(merged[-1][-1], num[-1])
    print(merged)