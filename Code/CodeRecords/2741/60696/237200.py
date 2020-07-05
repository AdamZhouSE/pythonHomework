def is_increase(nums):
    for i in range(len(nums)):
        if i+1 < len(nums) and nums[i] < nums[i+1]:
            pass
        elif i+1 == len(nums):
            pass
        else:
            return False
    return True


arr = [int(i) for i in input()[1:-1].split(',')]
sub_arrs = [arr[i:j] for i in range(0, len(arr)) for j in range(i+1, len(arr)+1)]
res = []
for sub_arr in sub_arrs:
    if is_increase(sub_arr):
        res.append(sub_arr)
print(max([len(i) for i in res]))