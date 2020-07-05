nums = input()
number = ""
start = False
end = False
if nums[0] != '-' and (nums[0] < '0' or nums[0] > '9') and nums[0] != ' ':
    print(0)
else:
    for n in nums:
        if end:
            break
        if n == ' ':
            continue
        elif n == '-' or (n >= '0' and n <= '9'):
            number += n
            start = True
            continue
        if start:
            if n < '0' or n > '9':
                end = True

if int(number) >= pow(2, 31) - 1:
    print(pow(2, 31) - 1)
elif int(number) <= -pow(2, 31):
    print(-pow(2, 31))
else:
    print(number)