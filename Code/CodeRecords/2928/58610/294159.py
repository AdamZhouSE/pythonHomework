vol = eval(input())
nums = list(zip(list(range(1, 10)), list(map(int, input().split(' ')))))
min_vol = min(reversed(nums), key=lambda x: x[1])

def get_max_num(rest):
    for i in range(8, -1, -1):
        if nums[i][1] <= rest:
            return nums[i][0], nums[i][1]

def sol():
    if vol < min_vol[1]:
        return -1
    temp_max = [min_vol[0]] * (vol // min_vol[1])
    rest_vol = vol % min_vol[1] + min_vol[1]
    index = 0
    while rest_vol > min_vol[1] and index < vol // min_vol[1]:
        num, used = get_max_num(rest_vol)
        temp_max[index] = num
        rest_vol = rest_vol - used + min_vol[1]
        index += 1
    return eval(''.join(str(i) for i in temp_max))
try:
    print(sol())
except Exception:
    print(nums)