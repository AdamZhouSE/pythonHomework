t = int(input())
for index in range(t):
    li = input().split(" ")
    row = int(li[0])
    column = int(li[1])
    numbers = input().split(" ")
    for i in range(column):
        print(numbers[i], end=" ")
    start = column - 1
    times = 1
    rl = row - 1
    cl = column - 1
    while rl > 0 and cl > 0:
        if times % 2 == 1:
            for j in range(rl):
                start += column
                print(numbers[start], end=" ")
            rl -= 1
            for i in range(cl):
                start -= 1
                print(numbers[start], end=" ")
            cl -= 1
        else:
            for j in range(rl):
                start -= column
                print(numbers[start], end=" ")
            rl -= 1
            for i in range(cl):
                start += 1
                print(numbers[start], end=" ")
            cl -= 1
        times += 1
    print("\n")
