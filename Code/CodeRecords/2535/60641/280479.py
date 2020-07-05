def main():
    nums = eval(input())
    print(segment(nums))


def segment(nums):
    result = 1
    lower_right = 0
    upper_left = len(nums)
    if len(nums) == 1:
        return result
    else:
        try:
            temp = nums + [max(nums) + 1]
            while nums[lower_right] < min(temp[lower_right + 1:]) and lower_right < upper_left:
                lower_right += 1
            if lower_right == len(nums):
                result = len(nums)
                return result
            else:
                if lower_right != 0:
                    result += segment(nums[:lower_right])
        except IndexError:
            return len(nums)

        try:
            temp = [min(nums) - 1] + nums
            while nums[upper_left - 1] > max(temp[:upper_left]) and lower_right < upper_left:
                upper_left -= 1
            if lower_right == upper_left:
                result = len(nums)
                return result
            else:
                if upper_left != len(nums):
                    result += segment(nums[upper_left:])
        except IndexError:
            return len(nums)

        if lower_right == 0 and upper_left == len(nums):
            return 1
        else:
            result = result + segment(nums[lower_right:upper_left]) - 1
            return result


if __name__ == '__main__':
    main()
