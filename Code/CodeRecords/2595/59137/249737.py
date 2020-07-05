def s2():
    num = int(input())
    for i in range(num):
        s = input().split()
        a = int(s[0])
        b = int(s[1])
        print(b ** (a-1))


s2()