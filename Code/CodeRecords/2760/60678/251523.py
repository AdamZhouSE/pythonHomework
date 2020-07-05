times = int(input())
for loopTimes in range(0, times):
    inputs = input().split()
    length = int(inputs[0])
    money = int(inputs[1])
    print(money * ( (length + 1) // 2))