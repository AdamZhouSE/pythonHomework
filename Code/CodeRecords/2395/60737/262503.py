def order(nums):
    ret = []
    count = 0
    for i in nums:
        if i==0:
            count += 1
        else:
            ret.append(i)
    while count:
        ret.append(0)
        count -= 1
    return ret


def exa(nums):
    l = len(nums)
    nums = order(nums)
    for i in range(l-1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0
            nums = order(nums)
    return nums


if __name__ == "__main__":
    t = int(input())
    while t:
        l = int(input())
        nums = [int(n) for n in input().split( )]
        ret = exa(nums)
        for j in range(l):
            print(ret[j], end="")
            if j != l-1:
                print(' ', end="")
        t -= 1
        print()