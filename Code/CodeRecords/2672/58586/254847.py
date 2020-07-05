nums = int(input())
for i in range(nums):
    num = int(input())
    if num==1:
        print(4294967294)
    else:
        arr = [0] * 32
        j = 0
        while num > 0:
            arr[i] = (1 ^ (num % 2))
            num = num // 2
            i += 1
        while i < 32:
            arr[i] = 1 - arr[i]
            i += 1
        i = 31
        sum = 0
        while i >= 0:
            sum = sum * 2 + arr[i]
            i -= 1
        print(sum)
        