for _ in range(eval(input())):
    a = list(map(int, input().split(' ')))
    print(1 if a[0]>=a[1]*(a[1] + 1) / 2 else 0)