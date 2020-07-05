def main():
    num = int(input())
    for i in range(0, num):
        length = int(input())
        nums = list(map(int, input().split(" ")))
        index = int(input())
        print(find(nums, index))


def find(nums, index):
    left = 0
    right = len(nums) - 1
    right_first = True
    while left != right:
        if right_first:
            if nums[left] > nums[right]:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right_first = False
            else:
                right -= 1
        else:
            if nums[left] > nums[right]:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                right -= 1
                right_first = True
            else:
                left += 1

    if len(nums) > 2:
        if left + 1 == index:
            return nums[left]
        elif left + 1 > index:
            return find(nums[:left], index)
        else:
            return find(nums[left + 1:], index - left - 1)
    else:
        return nums[index - 1]


if __name__ == "__main__":
    main()
