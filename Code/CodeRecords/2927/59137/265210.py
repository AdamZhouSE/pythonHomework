def s31():
    s = input().split()
    n = int(s[0])
    d = int(s[1])
    m = int(input())

    for i in range(m):
        s = input().split()
        x = int(s[0])
        y = int(s[1])
        if x-d <= y and y <= x+d and -x+d <= y and y <= -x+2*n-d:
            print("YES")
        else:
            print("NO")


s31()