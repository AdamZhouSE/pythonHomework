t = int(input())
for x in range(t):
    n = int(input())
    a = input().split()
    b = input().split()
    d = 0
    flag = 1
    for i in range(n):
        if a[i] != b[i]:
            if d == 0:
                d = int(a[i]) - int(b[i])
            else:
                if int(a[i]) - int(b[i]) != d:
                    flag = 0
                    break
    if flag:
        print("YES")
    else:
        print("NO")
