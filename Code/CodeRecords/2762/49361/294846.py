n = int(input())
status = ['N', 'W', 'S', 'E']
for i in range(n):
    t = int(input())
    arr = input()
    arr = arr.split(" ")
    x = 0
    y = 0
    currentStatus = 'N'

    for k in range(arr.__len__()):
        if k % 2 == 1:
            count = int(arr[k])
            # print(x, y)
            if currentStatus == 'N':
                y += count
            if currentStatus == 'S':
                y -= count
            if currentStatus == 'W':
                x -= count
            if currentStatus == 'E':
                x += count
        else:
            char = arr[k]
            index = status.index(currentStatus)
            if char == 'U':
                continue
            if char == 'D':
                currentStatus = status[index - 2]
                continue
            if char == 'L':
                currentStatus = status[index + 1]
                continue
            if char == 'R':
                currentStatus = status[index - 1]
                continue
    length = int((x * x + y * y) ** 0.5)
    print(length, end=" ")
    print(currentStatus)
