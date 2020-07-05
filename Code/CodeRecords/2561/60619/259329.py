t = int(input())
for ind in range(t):
    li = input().split()
    size = int(li[0])
    target = int(li[1])
    mar1 = []
    for i in range(size):
        ori = input().strip().split(" ")
        for j in ori:
            mar1.append(int(j))
    mar2 = []
    for i in range(size):
        ori = input().strip().split(" ")
        for j in ori:
            mar2.append(int(j))
    result = 0
    for i in mar1:
        if mar2.count(target-i) > 0:
            result += 1
    print(result)