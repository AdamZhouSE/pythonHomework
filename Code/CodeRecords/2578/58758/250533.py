def sum_av(nums, divisor):
    result = 0
    for i in nums:
        if i % divisor == 0:
            result += i//divisor
        else:
            result += i//divisor+1
    return result


nums = [int(x) for x in input().split(',')]
threshold = int(input())
i = 1
while True:
    if sum_av(nums, i) <= threshold:
        break
    i += 1
print(i)
