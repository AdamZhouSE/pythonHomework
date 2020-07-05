times = int(input())
nums = []
for i in range(times):
    nums.append(int(input()))


def trackBack(start, sum):
    if start == times:
        if sum == 0:
            return True
        else:
            return False
    else:
        if trackBack(start + 1, (sum + nums[start]+360)%360):
            return True
        if trackBack(start + 1, (sum - nums[start]+360)%360 ):
            return True
        else:
            return False


if trackBack(0, 0):
    print("YES")
else:
    print("NO")
