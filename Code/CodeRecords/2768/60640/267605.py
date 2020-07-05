t = int(input())
for i in range(t):
    inp = input().split(" ")
    A, B, M = int(inp[0]), int(inp[1]), int(inp[2])
    count = 0
    if M <= B:
        start = A + max(A, M) % min(A, M)
        while start <= B:
            count += 1
            start += M
    print(count)
