T = int(input())

for i in range(T):
    rest = int(input()) % 5
    if rest == 0:
        print(-1)
    else:
        print(rest)
