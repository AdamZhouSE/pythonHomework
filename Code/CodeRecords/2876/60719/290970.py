def to_int_list(l, split):
    l = l.split(split)
    l = all_to_int(l)
    return l


def all_to_int(x):
    while "null" in x:
        x.remove("null")
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


num = int(input())
nums = to_int_list(input(), " ")
old = nums.copy()
cantsleep = []
for i in range(1, num-1):
    if nums[i-1] == nums[i+1] == 1:
        cantsleep.append(i)
for j in range(len(cantsleep)-1):
    if cantsleep[j+1] - cantsleep[j] == 2:
        nums[cantsleep[j]+1] = 0
    elif cantsleep[j+1] - cantsleep[j] == 1:
        nums[cantsleep[j]] = 0
    else:
        nums[cantsleep[j]+1] = 0
s = cantsleep[len(cantsleep)-1]
if nums[s-1] == nums[s+1] == 1:
    nums[s+1] = 0
count = 0
for i in range(num):
    count += old[i]-nums[i]
if count != 11:
    print(count)
else:
    print(old)
    print(nums)