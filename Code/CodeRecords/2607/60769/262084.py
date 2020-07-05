def cal(substr):
    count = [0, 0, 0]
    for item in substr:
        count[item] += 1
    if count[0] == count[1] and count[1] == count[2]:
        return 1
    else:
        return 0


num = int(input())
for j in range(num):
    arr = list(map(int, list(input())))
    sum = 0
    for i in range(3, len(arr) + 1, 3):
        for k in range(0, len(arr) - i+1):
            sum += cal(arr[k:k + i])
    print(sum)