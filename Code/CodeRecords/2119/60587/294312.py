nums = input().split(',')
num = [int(nums[i]) for i in range(len(nums))]
if len(num) < 4:
    print("False")
else:
    a, b, c, (d, e, f) = 0, 0, 0, num[:3]
    for i in range(3, len(num)):
        a, b, c, d, e, f = b, c, d, e, f, num[i]
        if e < c - a and f >= d:
            print("True")
        elif c - a <= e <= c and f >= (d if d - b < 0 else d - b):
            print("True")
        else:
            print("False")
