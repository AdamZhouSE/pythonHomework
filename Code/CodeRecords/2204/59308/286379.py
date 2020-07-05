T = int(input())
for _ in range(T):
    a = int(input())
    a = [_ for _ in range(1, a+1)]
    print(*a, end=' \n')