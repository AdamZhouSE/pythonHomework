def s15():
    n = int(input())
    nums = list(input().split())
    count = 0

    if n <= 3:
        print(count)
        return
    for i in range(n-2):
        if nums[i] == '1' and nums[i+1] == '0' and nums[i+2] == '1':
            nums[i+2] = '0'
            count = count + 1
    print(count)


s15()