nums = eval(input())


def majorityElement():
    def maj_rec(left, right):
        if left == right:
            return nums[right]

        center = (left + right) // 2
        left_maj = maj_rec(left, center)
        right_maj = maj_rec(center + 1, right)

        if left_maj == right_maj:
            return right_maj

        count_left_maj = 0
        for le in nums[left:center + 1]:
            if le == left_maj:
                count_left_maj += 1

        count_right_maj = 0
        for re in nums[center + 1: right + 1]:
            if re == right_maj:
                count_right_maj += 1

        if count_left_maj > count_right_maj:
            return left_maj
        else:
            return right_maj
    return maj_rec(0, len(nums) - 1)


print(majorityElement())
