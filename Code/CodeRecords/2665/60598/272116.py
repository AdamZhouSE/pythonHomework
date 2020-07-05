times = int(input())
for i in range(times):
    line = input().split(" ")
    x = int(line[0])
    y = int(line[1])
    z = int(line[2])
    temp = z
    count = 0
    while temp != 1:
        if x >= temp and x % temp == 0:
            count += 1
            x -= 1
        temp -= 1
    print(count, "", end="")
    count = 0
    temp = z
    while temp != 1:
        if y >= temp and y % temp == 0:
            count += 1
            y -= 1
        temp -= 1
    print(count)
