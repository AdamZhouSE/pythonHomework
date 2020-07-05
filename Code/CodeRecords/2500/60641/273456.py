def main():
    nums = eval(input())
    result = change(nums)
    print(result)


def change(nums):
    if len(nums) == 1:
        return []
    else:
        result = []
        if nums.index(max(nums)) != len(nums) - 1:
            if nums.index(max(nums)) == 0:
                result.append(len(nums))
                nums = list(reversed(nums))
            else:
                result.append(nums.index(max(nums))+1)
                temp = list(reversed(nums[0:nums.index(max(nums))+1]))
                nums = temp + nums[nums.index(max(nums))+1:]
                result.append(len(nums))
                nums = list(reversed(nums))
            result += change(nums[:len(nums) - 1])
        return result


if __name__ == "__main__":
    main()
