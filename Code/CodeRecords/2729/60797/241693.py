def singleNonDuplicate(nums):
    p = -1
    count = 0
    for x in nums:
        if p == -1:
            p = nums[0]
            count = 1
            continue
        if x == p and count == 1:
            count += 1
            continue
        elif x != p and count == 1:
            return p
        else:
            p = x
            count = 1
    return p

if __name__ == "__main__":
    data = [int(a) for a in input().strip("[]").split(",")]
    re = singleNonDuplicate(data)
    print(re)
