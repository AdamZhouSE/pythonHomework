def main():
    nums = input().split(',')
    print(max(nums))


def max(nums):
    if len(nums) == 1:
        return str(nums[0])
    else:
        result = str(nums[0])
        del nums[0]
        result = result + "/" + min(nums)
        return result


def min(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        result = nums[0]
        del nums[0]
        for num in nums:
            result = result + "/" + num
        result = "(" + result + ")"
        return result


if __name__ == '__main__':
    main()