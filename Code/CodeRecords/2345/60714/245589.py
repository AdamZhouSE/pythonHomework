n = int(input())
for i in range(0, n):
    length = int(input())
    num = dict()
    for item in [int(x) for x in input().split()]:
        if item in num:
            num[item] += 1
        else:
            num[item] = 1
    flag = False
    for j in range(1, n + 1):
        if j not in num:
            print(j, end=" ")
            flag = True
            break
    for j in num.keys():
        if num[j] is 2:
            print(j)
    if not flag:
        print("0 0")
