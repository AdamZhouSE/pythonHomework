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
nums.sort()
min = max = 0
big = nums[num-1]
small = nums[0]
mid = nums[num//2]
res = "YES"
if mid == big or mid == small:
    res = "NO"
for i in nums:
    if i == small:
        min += 1
    elif i == big:
        max += 1
    elif i != mid:
        res = "NO"
        break
if big == small:
    res = "YES"
print(res)