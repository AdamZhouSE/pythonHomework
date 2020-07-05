arr = input().split()
n = int(arr[0])
limit = int(arr[1])
if n == 0 or limit == 0:
    print('0')
    exit()
time_stamp = [int(i) for i in input().split()]
remain = 1
for i in range(1, len(time_stamp)):
    if time_stamp[i] - time_stamp[i-1] > limit:
        remain = 1
    else:
        remain += 1
print(remain)