a = int(input())
for i in range(a):
    b = int(input())
    c = list(input().split())
    sum = 0
    for i in range(c.__len__() - 2):
        for j in range(i + 1, c.__len__() - 1):
            for k in range(j + 1, c.__len__()):
                d = [int(c[i]), int(c[j]), int(c[k])]
                d.sort()
                if d[0] + d[1] > d[2]:
                    sum += 1
    print(sum)
