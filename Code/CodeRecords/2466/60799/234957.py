T = int(input())
for hhh in range(0, T):
    input()
    list = sorted([int(i) for i in input().split()])
    num = 0
    for i in range(0, len(list) - 2):
        for j in range(i + 1, len(list) - 1):
            for k in range(j + 1, len(list)):
                if (list[i] + list[j]) > list[k]:
                    print(list[i], list[j], list[k])
                    num += 1
    print(num)