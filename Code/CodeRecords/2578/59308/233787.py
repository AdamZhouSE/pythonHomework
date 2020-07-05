nums = [int(x) for x in input().split(",")]
threshold = int(input())
q = 1
while True:
    my_sum = 0
    for i in range(len(nums)):
        my_sum += int(nums[i]/q) + 1
    if my_sum <= threshold:
        print(q)
        break
    else:
        q = q + 1
