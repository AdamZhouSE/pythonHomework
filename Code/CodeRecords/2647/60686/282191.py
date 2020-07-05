nums = int(input())
list_num = []
for i in range(nums):
    num = int(input())
    list_num.append(num)
for i in range(nums):
    num = list_num[i]
    x = 0
    count = 0
    while pow(2, x) <= num:
        x += 1
    x -= 1
    while num > 0:
        if pow(2, x) <= num:
            num -= pow(2, x)
            count += 1
        else:
            x -= 1
    print(count)
