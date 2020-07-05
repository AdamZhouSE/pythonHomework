if __name__ == '__main__':
    res = []
    nums = [int(i) for i in input().split(',')]
    temp = [False for i in range(len(nums) + 1)]
    temp[0] = True
    for i in nums:
        if temp[i] is False:
            temp[i] = True
        else:
            res.append(i)
    for i in range(1, len(nums)+1):
        if temp[i] is False:
            res.append(i)
            break
    print(res)
