def c(a, b, start, n, m, N, M):
    global count, check
    if m == 0:
        # print(''.join(b))
        if b == check:
            count += 1
    else:
        # m > 0
        for i in range(start, N - m + 1):
            b[M - m] = a[i]
            c(a, b, i + 1, n - i - 1, m - 1, N, M)



n = int(input())
for i in range(0, n):
    input()
    inputs = input().split()
    string = list(inputs[0])
    check = inputs[1]

    # mission clean
    count = 0
    string = list(string)
    for i in range(len(string) - 1, -1, -1):
        if check.find(string[i]) == -1:
            del string[i]
    check = list(check)
    c(string, [" "] * len(check), 0, len(string), len(check), len(string), len(check))
    print(count)
