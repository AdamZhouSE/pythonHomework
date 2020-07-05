def min(n,num):
    basic = 2
    result = 0
    while(num != 1):
        num -= 1
        n -= 1
        result += basic
        basic *= 2
    return result + n

def max(n,num):
    basic = 1
    result = 0
    while (num != 0):
        num -= 1
        n -= 1
        result += basic
        basic *= 2
    return int(result + n * (basic / 2))

nums = list(map(int,input().split(" ")))
res = []
res.append(str(min(nums[0],nums[1])))
res.append(str(max(nums[0],nums[2])))
print(" ".join(res))