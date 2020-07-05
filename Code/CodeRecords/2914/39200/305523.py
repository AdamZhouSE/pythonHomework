t = int(input())
for x in range(t):
    n = int(input())
    a = input().split()
    b = input().split()
    d = 0
    flag = 1
    for i in range(n):
        if int(a[i]) < int(b[i]):
            if d == 0:
                d = int(b[i]) - int(a[i])
            else:
                if int(b[i]) - int(a[i]) != d:
                    flag = 0
                    break
        elif int(a[i]) > int(b[i]):
            flag = 0
            break
    if flag:
        print("YES")
    else:
        print("NO")
