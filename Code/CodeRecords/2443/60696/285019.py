if __name__ == '__main__':
    nums = [str(i) for i in input()[1:-1].split(',')]
    nums.sort(reverse=True)
    res = ''
    for num in nums:
        res += num
    print(int(res))