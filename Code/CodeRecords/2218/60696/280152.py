if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    nums.sort(key=lambda x: -abs(x))
    has_negative = False
    res_positive = 1
    res_negative = 1
    negative_cnt = 0
    positive_cnt = 0
    for i in range(len(nums)):
        if nums[i] >= 0:
            if positive_cnt <= 3:
                res_positive *= nums[i]
                positive_cnt += 1
            if positive_cnt == 1:
                res_negative *= nums[i]
        else:
            if negative_cnt < 2:
                res_negative *= nums[i]
                negative_cnt += 1
        if positive_cnt == 3 and negative_cnt == 2:
            break
    print(max(res_negative, res_positive))