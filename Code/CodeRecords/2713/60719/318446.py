def to_int(l):
    for i in range(len(l)):
        l[i] = int(l[i])
    return l


def check(s, start, end):
    point = s[start]
    for i in range(start+1, end):
        if s[i] < point and s[i] != 0:
            return False
    return True


def get(limit, nums):
    for i in range(limit[0]):
        if nums[i] == 0:
            if limit[1] not in nums:
                nums[i] = limit[1]
            else:
                if i == 0 or nums[i-1] == 0:
                    nums[i] = nums[1+i]
                elif i == limit[0]-1 or nums[i+1] == 0:
                    nums[i] = nums[i-1]
                else:
                    nums[i] = min(nums[i+1], nums[i-1])
            continue
        if nums[i] > limit[1]:
            return "NO"
        for j in range(i+1, limit[0]):
            if nums[i] == nums[j]:
                if not check(nums, i, j):
                    return "NO"
    return nums


limit = to_int(input().split(" "))
nums = to_int(input().split(" "))
res = get(limit, nums)
if res != "NO":
    print("YES")
    out = ''
    for x in nums:
        out += str(x)
        out += " "
    print(out)
else:
    print("NO")