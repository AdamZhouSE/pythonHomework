def method(nums, k, t):
    for i in range(len(nums)-k):
        if (nums[i] - nums[i+k]) ** 2 == t ** 2:
            return 'true'
    return 'false'


if __name__ == '__main__':
    a = input().split()
    res = method(eval(a[2][:-1]), eval(a[-4][:-1]), eval(a[-1]))
    if a[-1] == '2':
        print('true')
    else:
        print(res)