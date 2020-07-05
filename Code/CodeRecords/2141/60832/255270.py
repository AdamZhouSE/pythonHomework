All = int(input())

for q in range(0, All):
    n = int(input())
    for i in range(1, n + 1):
        print(bin(i)[2:], end=' ')
    print()
