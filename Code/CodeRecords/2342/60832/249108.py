All = int(input())

for i in range(0, All):
    temp = list(map(int, input().split(" ")))
    string = input()
    num = temp[0]
    groupNum = temp[1]
    lst = list(filter(None, string.split(" ")))
    lst2 = []
    for j in range(0, num // groupNum + 1):
        if j == num // groupNum:
            lst2 = lst2 + lst[:j * groupNum - num - 1:-1]
        else:
            lst2 = lst2 + lst[(j + 1) * groupNum - num - 1:j * groupNum - num - 1:-1]

    for j in range(0, len(lst2)):
        print(lst2[j], '', end='')
    print()
