def all_to_int(x):
    while "null" in x:
        x.remove("null")
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


def handle_each_use_case():
    n = int(input())
    if n % 5 == 0:
        return -1
    return n % 5


num = int(input())
nums = input().split(" ")
nums = all_to_int(nums)
copy = nums.copy()
copy.sort(reverse=True)
big = copy[0]
pos = nums.index(big)
res = "YES"
for i in range(1, num):
    if i <= pos:
        if nums[i-1] >= nums[i]:
            res = "NO"
            break
    else:
        if nums[i] != big:
            if nums[i-1] <= nums[i]:
                res = "NO"
                break
        else:
            if nums[i-1] < nums[i]:
                res = "NO"
                break
print(res)