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
count = 0
for i in range(1, num-1):
    if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
        count += 1
    elif nums[i-1] > nums[i] and nums[i] < nums[i+1]:
        count += 1
print(count)