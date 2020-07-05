def min_step(nums):
    nums = list(nums)
    below_zero = 0
    has_zero = False
    count = 0
    for each in nums:
        if each == 0:
            has_zero = True
            count += 1
        elif each < 0:
            below_zero += 1
            count += -1 - each
        else:
            count += each - 1
    if has_zero:
        return count
    elif below_zero%2 == 0:
        return count
    else:
        return count + 2


if __name__ == '__main__':
    input()
    nums = [int(i) for i in input().split()]
    print(min_step(nums))