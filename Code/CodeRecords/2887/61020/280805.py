n = int(input())

result_list = []
record = {}
for i in range(0, n):
    line = input()
    nums = line.split()

    if int(nums[0]) in record:
        record[int(nums[0])][0] += int(nums[1])
        record[int(nums[0])][1] += int(nums[2])
    else:
        record[int(nums[0])] = [int(nums[1]), int(nums[2])]

if record[1][0] >= record[1][1]:
    print("LIVE")
else:
    print("DEAD")

if record[2][0] >= record[2][1]:
    print("LIVE")
else:
    print("DEAD")
