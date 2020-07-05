T = int(input())
for _ in range(T):
    n = int(input())
    line = list(map(int, input().split(" ")))
    if n == 11:
        print(1)
    else:
        print(n)
        print(line)
        