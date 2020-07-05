num=int(input())
for i in range(num):
    input()
    first=[int(x) for x in input().split()]
    second = [int(x) for x in input().split()]
    for j in first:
        if j not in second:
            second.append(j)
    print(len(second))