def s22():
    n = int(input())
    s = input().split()
    last = max(int(s[0]), int(s[1]))

    for i in range(1, n):
        s = input().split()
        if int(s[1]) > last:
            if int(s[0]) > last:
                print("NO")
                return
            last = int(s[0])
    print("YES")


s22()