def tell_spell_num(nums):
    n = len(nums)
    sub_arrs = []
    for i in range(n):
        for j in range(i+1, n+1):
            if sub_arrs.__contains__(nums[i:j]):
                pass
            else:
                sub_arrs.append(nums[i:j])
    return len(sub_arrs)


if __name__ == '__main__':
    n = int(input())
    nums = []
    temp = [int(i) for i in input().split()]
    for i in range(n):
        nums.append(temp[i])
        print(tell_spell_num(nums))