times = int(input())
for loopTimes in range(0, times):
    inputs = input().split()
    m = int(inputs[0])
    n = int(inputs[1])
    a = int(inputs[2])
    b = int(inputs[3])
    count = 0
    for i in range(m, n + 1):
        if i / a == i // a or i / b == i // b:
            count += 1
    print(count)