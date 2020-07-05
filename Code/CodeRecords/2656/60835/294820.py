for q in range(int(input())):
    mn = list(map(int, input().split()))
    def to_binary(n):
        string = ""
        while n > 0:
            string = string + str(n % 2)
            n = n // 2
        return string
    m = to_binary(mn[0])
    n = to_binary(mn[1])
    if len(m) > len(n):
        length = len(n)
        for x in range(length,len(m)):
            n = n + "0"
    else:
        length = len(m)
        for x in range(length,len(n)):
            m = m + "0"
    x = 0
    while True:
        if x == len(m):
            break
        if n[x] != m[x]:
            break
        x = x + 1
    print(str(x + 1))
        
