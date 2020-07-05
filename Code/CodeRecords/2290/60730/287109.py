num = int(input())
for i in range(num):
    n = int(input())
    m = list(map(int, input().split(" ")))
    for j in range(len(m) - 1):
        if m[j] > m[j + 1]:
            print(m[j + 1], end=" ")
        else:
            print("-1", end=" ")
    print("-1 ")
