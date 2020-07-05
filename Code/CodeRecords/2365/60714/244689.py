n = int(input())
for i in range(0, n):
    m = int(input())
    temp = input().split()
    num = []
    length = max([len(x) for x in temp])
    for j in range(0, m):
        item = temp[j] + temp[j][-1] * (length - len(temp[j]))
        num.append((temp[j], item))
    num.sort(key=lambda x: x[1], reverse=True)
    for j in range(0, m - 1):
        print(num[j][0], end="")
    print(num[m - 1][0])
