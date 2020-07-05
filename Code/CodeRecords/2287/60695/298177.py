t = int(input())
for i in range(t):
    n = int(input())
    a = input().split(" ")
    a = list(map(int, a))
    for j in range(0, n - 1):
        flag = True
        for k in range(j+ 1, n):
            if a[k] >= a[j]:
                print(str(a[k]) + " ", end="")
                flag = False
                break
        if flag:
            print("-1 ", end="")
    print("-1")
