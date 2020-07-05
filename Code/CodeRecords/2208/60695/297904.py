t = int(input())
for i in range(t):
    n = int(input())
    a = input().split(" ")
    a = list(map(int, a))
    print("-1 ", end="")
    for j in range(1, n-1):
        flag = True
        for k in range(j - 1, -1, -1):
            if a[k] < a[j]:
                print(str(a[k]) + " ", end="")
                flag = False
                break
        if flag:
            print("-1 ", end="")
    flag = True
    for k in range(n - 2, -1, -1):
        if a[k] < a[n-1]:
            print(str(a[k]))
            flag = False
            break
    if flag:
        print("-1")
    