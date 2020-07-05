num = int(input())
row = list(map(int, input().split()))
row = sorted(row)
if len(row) == 1:
    print(1)
elif len(row) == 2:
    print(2)
else:
    test = [row[0], row[1]]
    tmp = 2
    for i in range(1, num - 1):
        if sum(test) <= row[i + 1]:
            tmp = tmp + 1
            test.append(row[i + 1])
        else:
            continue
    print(tmp)
