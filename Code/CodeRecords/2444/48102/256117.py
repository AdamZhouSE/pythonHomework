import re


def find_repeat(nums: list, k: int, t: int) -> bool:
    if t < 0:
        return False
    table = {}
    nums_len = len(nums)
    w = t + 1
    for i in range(nums_len):
        if i > k:
            del table[get_id(nums[i-k-1], w)]
        id = get_id(nums[i], w)
        if id in table.keys():
            return True
        if id + 1 in table.keys() and abs(table[id+1] - nums[i]) <= t:
            return True
        if id - 1 in table.keys() and abs(table[id-1] - nums[i]) <= t:
            return True
        table[id] = nums[i]
    return False


def get_id(num: int, w: int) -> int:
    if num > 0:
        return num // w
    else:
        return (num + 1) // w - 1


string = input()
match_obj = re.match(r'nums = (.*), k = (.*), t = (.*)', string)
n = eval(match_obj.group(1))
k_in = int(match_obj.group(2))
t_in = int(match_obj.group(3))
if find_repeat(n, k_in, t_in):
    print('true')
else:
    print('false')