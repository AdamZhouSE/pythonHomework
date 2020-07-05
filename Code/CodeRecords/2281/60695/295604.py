t = int(input())
for i in range(t):
    n = int(input())
    a = input().split(" ")
    a = list(map(int, a))
    for i in range(n - 1):
        flag = True
        for j in range(i + 1, n):
            if a[i] < a[j]:
                flag = False
        if flag:
            print(str(a[i]) + " ", end="")
    print(a[n - 1])
