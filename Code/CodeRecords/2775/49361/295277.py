t = int(input())
for i in range(t):
    l = int(input())
    if l % 3 == 0:
        print(l // 3 - 1, end=" ")
        print(l // 3, end=" ")
        print(l // 3 + 1)
    else:
        print(-1)
