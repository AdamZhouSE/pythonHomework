limit = int(input()[-1])
time_stamp = [int(i) for i in input().split()]
remain = 1
for i in range(1, len(time_stamp)):
    if time_stamp[i] - time_stamp[i-1] > limit:
        remain = 1
    else:
        remain += 1
print(remain)
