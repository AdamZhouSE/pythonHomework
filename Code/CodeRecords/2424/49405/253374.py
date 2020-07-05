T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    t = 0
    for num in a:
        t ^= num
    print(t)